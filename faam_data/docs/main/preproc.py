import glob
import json
import shutil
from typing import Mapping
import os
import sys
sys.path.insert(0, '../../')
from attributes import GlobalAttributes, GroupAttributes, VariableAttributes

global_schema = GlobalAttributes.model_json_schema()
group_schema = GroupAttributes.model_json_schema()
variable_schema = VariableAttributes.model_json_schema()


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

def attr_text(attr: str, properties: Mapping) -> str:
    txt = f'* ``{attr}`` - '

    _type = None
    _example = None

    try:
        _type = properties[attr]['type']
    except KeyError:
        pass

    try:
        _example = properties[attr]['example']
    except KeyError:
        pass

    try:
        _type = properties[attr]['anyOf']
        _type = '|'.join([i['type'] for i in _type])
    except KeyError:
        pass

    if _type is not None:
        txt += f'[{_type}] '

    txt += f'{properties[attr]["description"]}'

    if not txt.endswith('.'):
        txt += '.'
    txt += ' '

    if _example is not None:
        txt += f'Example: {_example}'

    txt += '\n'

    return txt

def make_global_attrs_rst() -> None:
    with open(os.path.join(dynamic_dir, 'metadata.rst'), 'r') as global_template:
        text = global_template.read()

    req_glob_text = ''
    opt_glob_text = ''

    properties = global_schema['properties']
    required = global_schema['required']

    for attr in properties:
        if attr in required:
            req_glob_text += attr_text(attr, properties)
        else:
            opt_glob_text += attr_text(attr, properties)


    text = text.replace('TAG_REQUIRED_GLOBAL_ATTRIBUTES', req_glob_text)
    text = text.replace('TAG_OPTIONAL_GLOBAL_ATTRIBUTES', opt_glob_text)

    with open(os.path.join(dynamic_dir, 'metadata.rst'), 'w') as f:
        f.write(text)

def make_group_attrs_rst() -> None:
    with open(os.path.join(dynamic_dir, 'metadata.rst'), 'r') as template:
        text = template.read()

    req_text = ''
    opt_text = ''

    properties = group_schema['properties']

    try:
        required = group_schema['required']
    except KeyError:
        required = []

    for attr in properties:
        if attr in required:
            req_text += attr_text(attr, properties)
        else:
            opt_text += attr_text(attr, properties)

    text = text.replace('TAG_REQUIRED_GROUP_ATTRIBUTES', req_text)
    text = text.replace('TAG_OPTIONAL_GROUP_ATTRIBUTES', opt_text)

    with open(os.path.join(dynamic_dir, 'metadata.rst'), 'w') as f:
        f.write(text)

def make_variable_attrs_rst() -> None:
    with open(os.path.join(dynamic_dir, 'metadata.rst'), 'r') as template:
        text = template.read()

    req_text = ''
    opt_text = ''

    properties = variable_schema['properties']

    try:
        required = variable_schema['required']
    except KeyError:
        required = []

    for attr in properties:
        if attr in required:
            req_text += attr_text(attr, properties)
        else:
            opt_text += attr_text(attr, properties)

    text = text.replace('TAG_REQUIRED_VARIABLE_ATTRIBUTES', req_text)
    text = text.replace('TAG_OPTIONAL_VARIABLE_ATTRIBUTES', opt_text)

    with open(os.path.join(dynamic_dir, 'metadata.rst'), 'w') as f:
        f.write(text)

def delete_dynamic_metadata() -> None:
    try:
        os.remove(os.path.join(dynamic_dir, 'metadata.rst'))
    except Exception:
        pass

def copy_metadata_template() -> None:
    shutil.copy2(
        os.path.join(template_dir, 'metadata.rst'),
        os.path.join(dynamic_dir, 'metadata.rst'),
    )


def make_metadata_section() -> None:
    delete_dynamic_metadata()
    copy_metadata_template()
    make_global_attrs_rst()
    make_group_attrs_rst()
    make_variable_attrs_rst()

def add_product(definition):
    with open(definition, 'r') as f:
        data = json.load(f)

    with open(os.path.join(dynamic_dir, 'products.rst'), 'a') as f:
        name = os.path.basename(definition.replace('.json', ''))
        f.write(name + '\n')
        f.write('-'*len(name) + '\n\n')
        f.write(':Name: ' + data['meta']['canonical_name'] + '\n')
        f.write(':Pattern: ``' + data['meta']['file_pattern'] + '``\n')
        f.write(':Description: ' + data['meta']['description'] + '\n')
        f.write(':References: ')
        f.write(' | '.join([f'`{i[0]} <{i[1]}>`_' for i in data['meta']['references']]))
        f.write('\n')
        f.write(':Details: ' + f'`{name} <https://www.faam.ac.uk/sphinx/data/product/{name}>`_\n')
        f.write(':Definition: ' + f'`{name}.json <https://github.com/FAAM-146/faam-data/tree/main/products/latest/{name}.json>`_ [on Github]\n')
        f.write(':Example data: ' + f'`{name} <https://drive.google.com/drive/folders/10jBV0odRNR6Yk7EbZHHyHGRlzvsAjFpl?usp=sharing>`_ [on Google Drive]')
        f.write('\n\n')


def make_products_section() -> None:
    TITLE = 'FAAM Data Products'
    definition_dir = '../../../products'
    files = [
        i for i in
        glob.glob(os.path.join(definition_dir, 'latest', '*'))
        if 'schema' not in i
    ]

    with open(os.path.join(dynamic_dir, 'products.rst'), 'w') as f:
        f.write(f'{"="*len(TITLE)}\n')
        f.write(f'{TITLE}\n')
        f.write(f'{"="*len(TITLE)}\n\n')

    for f in files:
        add_product(f)



if __name__ == '__main__':
    make_metadata_section()
    make_products_section()

