from typing import Mapping
import os
import sys
import glob
import shutil
sys.path.insert(0, '../../')
import json

TITLE = 'Faam Data Products'

def add_product(definition):
    with open(definition, 'r') as f:
        data = json.load(f)

    with open('index.rst', 'a') as f:
        name = os.path.basename(definition.replace('.json', ''))
        f.write(name + '\n')
        f.write('-'*len(name) + '\n\n')
        f.write(':Name: ' + data['meta']['canonical_name'] + '\n')
        f.write(':Pattern: ``' + data['meta']['file_pattern'] + '``\n')
        f.write(':Description: ' + data['meta']['description'] + '\n')
        f.write(':References: ')
        f.write(' | '.join([f'`{i[0]} <{i[1]}>`_' for i in data['meta']['references']]))
        f.write('\n\n')


if __name__ == '__main__':
    definition_dir = '../../products'
    files = [
        i for i in
        glob.glob(os.path.join(definition_dir, 'latest', '*'))
        if 'schema' not in i
    ]


    with open('index.rst', 'w') as f:
        f.write(f'{"="*len(TITLE)}\n')
        f.write(f'{TITLE}\n')
        f.write(f'{"="*len(TITLE)}\n\n')

    for f in files:
        add_product(f)
