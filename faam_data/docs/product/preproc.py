import glob
import json
import shutil
from typing import Mapping
import os
import sys
sys.path.append('../../')
from attributes import GlobalAttributes


template_dir = os.path.join(
    os.path.dirname(__file__),
    'templates'
)
dynamic_dir = os.path.join(
    os.path.dirname(__file__),
    'dynamic_content'
)

if not os.path.exists(dynamic_dir):
    os.makedirs(dynamic_dir)

# Expected to be 'html' or 'latexpdf'
BUILD_TARGET = sys.argv[1]


def init() -> None:
    for f in os.listdir(dynamic_dir):
        os.remove(f)

def copy_introduction() -> None:
    shutil.copy2(
        os.path.join(template_dir, 'introduction.rst'),
        os.path.join(dynamic_dir, 'introduction.rst'),
    )

def get_references(references: list[list[str,str]|dict], build_target:str=BUILD_TARGET) -> str:
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
        return 'None provided'
    
    if isinstance(ref1, list):
        return ' | '.join([f'`{i[0]} <{i[1]}>`_' for i in references])
    
    build_refs = []
    for ref in references:
        if build_target == 'html':
            try:
                build_refs.append(f'`{ref["title"]} <{ref["web"]}>`_')
            except KeyError:
                build_refs.append(f'`{ref["title"]} <https://doi.org/{ref["doi"]}>`_')
        else:
            try:
                build_refs.append(f'`{ref["title"]} <https://doi.org/{ref["doi"]}>`_')
            except KeyError:
                build_refs.append(f'`{ref["title"]} <{ref["web"]}>`_')
            
    return ' | '.join(build_refs)


def populate_introduction(definition) -> None:
    with open(definition, 'r') as f:
        data = json.load(f)

    name = os.path.basename(definition.replace('.json', ''))
    description = data['meta']['description']
    pattern = data['meta']['file_pattern']
    references = data['meta']['references']

    references = get_references(references)

    with open(os.path.join(dynamic_dir, 'introduction.rst'), 'r') as f:
        rst = f.read()

    rst = rst.replace('TAG_PRODUCT_NAME', name)
    rst = rst.replace('TAG_PRODUCT_DESCRIPTION', description)
    rst = rst.replace('TAG_PRODUCT_FILE_PATTERN', pattern)
    rst = rst.replace('TAG_PRODUCT_REFERENCES', references)

    with open(os.path.join(dynamic_dir, 'introduction.rst'), 'w') as f:
        f.write(rst)

def copy_global_attrs() -> None:
    shutil.copy(
        os.path.join(template_dir, 'global_attributes.rst'),
        os.path.join(dynamic_dir, 'global_attributes.rst'),
    )

def populate_global_attrs(definition) -> None:
    
    with open(definition, 'r') as f:
        data = json.load(f)
    attributes = data['attributes']

    text = ''
    for key, value in attributes.items():
        text += f'* ``{key}``: '
        text += f'**{value}** - '
        desc =  GlobalAttributes.model_json_schema()['properties'][key]['description']
        print(desc)
        text += desc + '\n'
    text += '\n'

    with open(os.path.join(dynamic_dir, 'global_attributes.rst'), 'r') as f:
        rst = f.read()

    rst = rst.replace('TAG_PRODUCT_GLOBAL_ATTRIBUTES', text)


    with open(os.path.join(dynamic_dir, 'global_attributes.rst'), 'w') as f:
        f.write(rst)

def copy_variables() -> None:
    shutil.copy(
        os.path.join(template_dir, 'variables.rst'),
        os.path.join(dynamic_dir,  'variables.rst'),
    )

def populate_variables(definition) -> None:
    with open(definition, 'r') as f:
        data = json.load(f)
    variables = sorted(data['variables'], key=lambda x: x['meta']['name'])
    text = ''
    for var in variables:
        _name =  f'{var["meta"]["name"]}'#' `{var["meta"]["datatype"]}`'
        text += _name + '\n'
        text += '-' * (len(_name)) + '\n'
        # text += f'* **{var["meta"]["name"]}** `{var["meta"]["datatype"]}`\n\n'
        text += f':Datatype: `{var["meta"]["datatype"]}`\n'
        text += f':Dimensions: {", ".join(var["dimensions"])}\n\n'
        #text += '\nAttributes\n'
        #text += '='* len('Attributes') + '\n\n'
        for attr_key, attr_value in var['attributes'].items():
            text += f'* ``{attr_key}`` : {str(attr_value)}\n'
        text += '\n'

    with open(os.path.join(dynamic_dir, 'variables.rst'), 'r') as f:
        rst = f.read()

    rst = rst.replace('TAG_PRODUCT_VARIABLES', text)


    with open(os.path.join(dynamic_dir, 'variables.rst'), 'w') as f:
        f.write(rst)


if __name__ == '__main__':
    definition = os.environ['FAAM_PRODUCT'] #/home/dave/vcs/faam-data/products/latest/core_faam_YYYYmmdd_v005_rN_xNNN.json'
    copy_introduction()
    populate_introduction(definition)
    copy_global_attrs()
    populate_global_attrs(definition)
    copy_variables()
    populate_variables(definition)


