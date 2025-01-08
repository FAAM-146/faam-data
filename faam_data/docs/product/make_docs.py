#!/usr/bin/env python

import argparse
import glob
import os
import shutil
import subprocess


def post_build_latexpdf(product_name: str, output_dir: str) -> None:
    """
    Move the built pdf to the output directory, and remove the build directory

    Args:
        product_name (str): The name of the product
        output_dir (str): The directory to output the documentation
    """

    pdf_file = glob.glob(os.path.join(f"_{product_name}", "latex", "*.pdf"))
    if len(pdf_file) != 1:
        raise Exception("Could not find pdf file")
    shutil.move(
        pdf_file[0],
        output_dir,
    )
    shutil.rmtree(f"_{product_name}")


def post_build_publish(product_name: str, output_dir: str) -> None:
    """
    Remove the build directory

    Args:
        product_name (str): The name of the product
        output_dir (str): The directory to output the documentation
    """

    shutil.rmtree(f"_{product_name}")


post_build_map = {
    f.replace("post_build_", ""): globals()[f]
    for f in globals()
    if f.startswith("post_build")
}


def make_doc(def_file: str, version: str, output_dir: str, target: str) -> None:
    """
    Build the documentation for a single product definition file

    Args:
        def_file (str): The path to the product definition file
        version (str): The version of the product
        output_dir (str): The directory to output the documentation
        target (str): The sphinx target to build
    """

    product_name = os.path.basename(def_file).replace(".json", "")
    newenv = os.environ.copy()
    newenv["FAAM_PRODUCT"] = def_file
    newenv["PRODUCT_VERSION"] = version
    subprocess.run(["make", target], env=newenv)

    try:
        post_build_map[target](product_name, output_dir)
    except KeyError:
        pass


def make_output_dir(output_dir: str) -> None:
    """
    Create the output directory if it does not exist

    Args:
        output_dir (str): The directory to output the documentation
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def make_docs(product_dir: str, version: str, output_dir: str, target) -> None:
    """
    Build the documentation for all product definitions in a directory

    Args:
        product_dir (str): The directory containing the product definitions
        version (str): The version of the product
        output_dir (str): The directory to output the documentation
        target (str): The sphinx target to build
    """

    make_output_dir(output_dir)
    definition_dir = os.path.join(product_dir, f"v{version}")
    definition_files = [
        os.path.join(definition_dir, f)
        for f in os.listdir(definition_dir)
        if f.endswith(".json") and "dataset_schema" not in f
    ]

    for definition in definition_files:
        make_doc(definition, version, output_dir, target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create documentation for data products"
    )
    parser.add_argument(
        "product_dir", type=str, help="The directory containing the product definitions"
    )
    parser.add_argument(
        "--version", "-v", type=str, default="latest", help="The version of the product"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="output",
        help="The directory to output the documentation",
    )
    parser.add_argument(
        "--target", "-t", type=str, default="latexpdf", help="The target to build"
    )
    args = parser.parse_args()
    make_docs(args.product_dir, args.version, args.output, args.target)
