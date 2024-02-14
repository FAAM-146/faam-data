import os
import glob
import yaml

from . import models
from . import attributes
from . import defaults

from .attributes import GlobalAttributes, VariableAttributes, GroupAttributes
from .models import Dataset
    
def get_product(short_name: str) -> Dataset | None:
    this_dir = os.path.dirname(__file__)
    products_dir = os.path.join(this_dir, '../products/latest')

    defs = [
        i for i in glob.glob(os.path.join(products_dir, '*.json'))
        if not i.endswith('dataset_schema.json')
    ]

    for d in defs:
        with open(d, 'r') as y:
            spec = yaml.load(y, Loader=yaml.Loader)
            try:
                if spec['meta']['short_name'] == short_name:
                    return Dataset.model_validate(spec)
            except Exception:
                continue

    return None

def get_spec(short_name: str) -> dict | None:
    this_dir = os.path.dirname(__file__)
    products_dir = os.path.join(this_dir, '../products/latest')

    defs = [
        i for i in glob.glob(os.path.join(products_dir, '*.json'))
        if not i.endswith('dataset_schema.json')
    ]

    for d in defs:
        with open(d, 'r') as y:
            spec = yaml.load(y, Loader=yaml.Loader)
            try:
                if spec['meta']['short_name'] == short_name:
                    return spec
            except Exception:
                continue

    return None
