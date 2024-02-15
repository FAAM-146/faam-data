import functools
import sys

from . import models
from . import attributes
from . import defaults
from .filecodec import filecodec

from .attributes import GlobalAttributes, VariableAttributes, GroupAttributes
from .models import Dataset
    
from vocal.utils import get_dataset as vocal_get_dataset
from vocal.utils import get_spec as vocal_get_spec

get_dataset = functools.partial(vocal_get_dataset, project=sys.modules[__name__])
get_spec = functools.partial(vocal_get_spec, project=sys.modules[__name__])
