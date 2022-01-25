
from pydantic import BaseModel
from typing import Union

from vocal.netcdf.mixins import DimensionNetCDFMixin

class Dimension(BaseModel, DimensionNetCDFMixin):
    name: str
    size: Union[int, None]
