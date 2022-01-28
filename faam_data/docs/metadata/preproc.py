from typing import Mapping
import os
import sys
sys.path.insert(0, '../../')
from attributes import GlobalAttributes, GroupAttributes, VariableAttributes

global_schema = GlobalAttributes.schema()
group_schema = GroupAttributes.schema()
variable_schema = VariableAttributes.schema()

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
    with open(os.path.join(template_dir, 'globals.rst'), 'r') as global_template:
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

    with open(os.path.join(dynamic_dir, 'globals.rst'), 'w') as f:
        f.write(text)

def make_group_attrs_rst() -> None:
    with open(os.path.join(template_dir, 'groups.rst'), 'r') as template:
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

    with open(os.path.join(dynamic_dir, 'groups.rst'), 'w') as f:
        f.write(text)

def make_variable_attrs_rst() -> None:
    with open(os.path.join(template_dir, 'variables.rst'), 'r') as template:
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

    with open(os.path.join(dynamic_dir, 'variables.rst'), 'w') as f:
        f.write(text)


if __name__ == '__main__':
    make_global_attrs_rst()
    make_group_attrs_rst()
    make_variable_attrs_rst()

