
from typing import Optional
import netCDF4 # type: ignore

from pydantic import BaseModel, Field

from vocal.netcdf.mixins import DatasetNetCDFMixin

from attributes import GlobalAttributes

from .dimension import Dimension
from .group import Group
from .variable import Variable


class DatasetMeta(BaseModel):
    file_pattern: str = Field(description='Canonical filename pattern for this dataset')
    canonical_name: Optional[str] = Field('Canonical name of this dataset')
    description: Optional[str] = Field(description='Description of the dataset')
    references: Optional[list[tuple[str, str]]] = Field(description='References for this dataset')


class Dataset(BaseModel, DatasetNetCDFMixin):
    class Config:
        title = 'FAAM Dataset Schema'

    meta: DatasetMeta
    attributes: GlobalAttributes
    dimensions: list[Dimension]
    groups: Optional[list[Group]]
    variables: list[Variable]
