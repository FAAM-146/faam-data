
from __future__ import annotations
from typing import Optional

from pydantic import BaseModel
from vocal.netcdf.mixins import GroupNetCDFMixin

from attributes import GroupAttributes

from .dimension import Dimension
from .variable import Variable

class GroupMeta(BaseModel):
    class Config:
        title = 'Group Metadata'

    name: str

class Group(BaseModel, GroupNetCDFMixin):
    class Config:
        title = 'Group Schema'

    meta: GroupMeta
    attributes: GroupAttributes
    dimensions: Optional[list[Dimension]]
    groups: Optional[list[Group]]
    variables: list[Variable]

Group.update_forward_refs()
