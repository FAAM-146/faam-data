import glob
import json
import shutil
from typing import Mapping, Any
import os
import sys

sys.path.insert(0, "../../")
from attributes import GlobalAttributes, GroupAttributes, VariableAttributes

global_schema = GlobalAttributes.model_json_schema()
group_schema = GroupAttributes.model_json_schema()
variable_schema = VariableAttributes.model_json_schema()

# Define the directories for the templates and dynamic(generated) content
template_dir = os.path.join(os.path.dirname(__file__), "templates")
dynamic_dir = os.path.join(os.path.dirname(__file__), "dynamic_content")

if not os.path.exists(dynamic_dir):
    os.makedirs(dynamic_dir)

# Expected to be 'html' or 'latexpdf'
BUILD_TARGET = sys.argv[1]


def attr_text(attr: str, properties: Mapping) -> str:
    """
    Create a string of text for an attribute in the metadata schema.

    Args:
        attr: The attribute name
        properties: The schema properties of the object

    Returns:
        str: A string of text for the attribute in rst format
    """
    txt = f"* ``{attr}`` - "

    _type = None
    _example = None

    try:
        _type = properties[attr]["type"]
    except KeyError:
        pass

    try:
        _example = properties[attr]["example"]
    except KeyError:
        pass

    try:
        _type = properties[attr]["anyOf"]
        _type = "|".join([i["type"] for i in _type])
    except KeyError:
        pass

    if _type is not None:
        txt += f"[{_type}] "

    txt += f'{properties[attr]["description"]}'

    if not txt.endswith("."):
        txt += "."
    txt += " "

    if _example is not None:
        txt += f"Example: {_example}"

    txt += "\n"

    return txt


def make_attrs_rst(schema: dict[str, Any], required_tag, optional_tag: str) -> None:
    """
    Create the global attributes section of the metadata.rst file
    """

    with open(os.path.join(dynamic_dir, "metadata.rst"), "r") as _template:
        text = _template.read()

    req_text = ""
    opt_text = ""

    properties = schema["properties"]
    try:
        required = schema["required"]
    except KeyError:
        required = []

    # Loop through the properties and create the text for each attribute
    for attr in properties:
        if attr in required:
            req_text += attr_text(attr, properties)
        else:
            opt_text += attr_text(attr, properties)

    # Replace the tags in the template with the generated text
    text = text.replace(required_tag, req_text)
    text = text.replace(optional_tag, opt_text)

    # Write the updated text to the metadata.rst file
    with open(os.path.join(dynamic_dir, "metadata.rst"), "w") as f:
        f.write(text)


def delete_dynamic_metadata() -> None:
    """
    Delete the dynamic metadata.rst file if it exists
    """
    try:
        os.remove(os.path.join(dynamic_dir, "metadata.rst"))
    except Exception:
        pass


def copy_metadata_template() -> None:
    """
    Copy the metadata.rst template to the dynamic_content directory
    """
    shutil.copy2(
        os.path.join(template_dir, "metadata.rst"),
        os.path.join(dynamic_dir, "metadata.rst"),
    )


def make_metadata_section() -> None:
    """
    Create the metadata section of the documentation
    """

    # Define the tags to replace in the metadata.rst template
    tags = [
        ["TAG_REQUIRED_GLOBAL_ATTRIBUTES", "TAG_OPTIONAL_GLOBAL_ATTRIBUTES"],
        ["TAG_REQUIRED_GROUP_ATTRIBUTES", "TAG_OPTIONAL_GROUP_ATTRIBUTES"],
        ["TAG_REQUIRED_VARIABLE_ATTRIBUTES", "TAG_OPTIONAL_VARIABLE_ATTRIBUTES"],
    ]

    # Define the schemas to use for the metadata
    schemas = (global_schema, group_schema, variable_schema)

    # Clean up the dynamic content directory
    delete_dynamic_metadata()
    copy_metadata_template()

    # Create the metadata section for each schema
    for schema, tags in zip(schemas, tags):
        make_attrs_rst(schema, *tags)


def get_references(
    references: list[list[str, str] | dict[str, str]], build_target: str = BUILD_TARGET
) -> str:
    """
    Get a string of references in rst format for inclusion in the documentation.

    References should be a list of lists, where each inner list contains a title and a URL,
    or a dictionary with keys `title` and `doi` and/or `web`. When compiling
    to html, the `web` key will be preferred over the `doi` key, when compiling
    to pdf, the `doi` key will be preferred over the `web` key.

    Args:
        references: A list of references
        build_target: The target format to build the references for. Can be `html` or `latexpdf`

    Returns:
        str: A string of references in rst format
    """

    try:
        ref1 = references[0]
    except IndexError:
        return "None provided"

    if isinstance(ref1, list):
        return " | ".join([f"`{i[0]} <{i[1]}>`_" for i in references])

    build_refs = []
    for ref in references:
        if build_target == "html":
            try:
                build_refs.append(f'`{ref["title"]} <{ref["web"]}>`_')
            except KeyError:
                build_refs.append(f'`{ref["title"]} <https://doi.org/{ref["doi"]}>`_')
        else:
            try:
                build_refs.append(f'`{ref["title"]} <https://doi.org/{ref["doi"]}>`_')
            except KeyError:
                build_refs.append(f'`{ref["title"]} <{ref["web"]}>`_')

    return " | ".join(build_refs)


def add_product(definition: str) -> None:
    """
    Add a product to the products.rst file

    Args:
        definition: The path to the product definition file
    """

    with open(definition, "r") as f:
        data = json.load(f)

    with open(os.path.join(dynamic_dir, "products.rst"), "a") as f:
        def_name = os.path.basename(definition.replace(".json", ""))
        name = data["meta"]["long_name"]
        f.write(name + "\n")
        f.write("-" * len(name) + "\n\n")
        f.write(":Name: " + data["meta"]["long_name"] + "\n")
        f.write(":Pattern: ``" + data["meta"]["file_pattern"] + "``\n")
        f.write(":Description: " + data["meta"]["description"] + "\n")
        f.write(":References: ")
        f.write(get_references(data["meta"]["references"]))
        f.write("\n")
        f.write(
            ":Details: "
            + f"`{name} <https://www.faam.ac.uk/sphinx/data/product/{def_name}>`_\n"
        )
        f.write(
            ":Definition: "
            + f"`{def_name}.json <https://github.com/FAAM-146/faam-data/tree/main/products/latest/{def_name}.json>`_ [on Github]\n"
        )
        f.write(
            ":Example data: "
            + f"`{name} <https://drive.google.com/drive/folders/10jBV0odRNR6Yk7EbZHHyHGRlzvsAjFpl?usp=sharing>`_ [on Google Drive]"
        )
        f.write("\n\n")


def make_products_section(title: str) -> None:
    """
    Build the products section of the documentation. This adds a small
    information block for each product in the products directory.

    Args:
        title: The title of the section
    """

    definition_dir = "../../../products"
    files = [
        i
        for i in glob.glob(os.path.join(definition_dir, "latest", "*"))
        if "schema" not in i
    ]

    with open(os.path.join(dynamic_dir, "products.rst"), "w") as f:
        f.write(f'{"="*len(title)}\n')
        f.write(f"{title}\n")
        f.write(f'{"="*len(title)}\n\n')

    for f in files:
        add_product(f)


if __name__ == "__main__":
    make_metadata_section()
    make_products_section("FAAM Data Products")
