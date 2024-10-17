
from typing import Optional
import netCDF4 # type: ignore

from pydantic import BaseModel, ConfigDict

from vocal.field import Field
from vocal.mixins import VocalDatasetMixin

from ..attributes import GlobalAttributes

from .dimension import Dimension
from .group import Group
from .variable import Variable

class FAAMDataReference(BaseModel):
    model_config = ConfigDict(
        title = 'FAAM Data Reference Schema'
    )

    title: str = Field(
        description='A brief title for the reference',
        example='Some paper',
    )

    doi: Optional[str] = Field(
        description='The DOI of the reference',
        example='10.1234/5678',
        default=None
    )

    web: Optional[str] = Field(
        description='A URL for the reference',
        example='https://www.example.com',
        default=None
    )

class DatasetMeta(BaseModel):
    file_pattern: str = Field(description='Canonical filename pattern for this dataset')
    short_name: Optional[str] = Field(
        description='A short name which can be used to uniquely identify this product',
        default=None
    )
    canonical_name: Optional[str] = Field(
        description='Canonical name of this dataset',
        default=None
    )
    description: Optional[str] = Field(
        description='Description of the dataset',
        default=None
    )
    references: Optional[list[FAAMDataReference]|tuple[str,str]] = Field(
        description='References for this dataset',
        default=None
    )


class Dataset(BaseModel, VocalDatasetMixin):
    model_config = ConfigDict(
        title = 'FAAM Dataset Schema'
    )

    meta: DatasetMeta
    attributes: GlobalAttributes
    dimensions: list[Dimension]
    groups: Optional[list[Group]] = None
    variables: list[Variable]
