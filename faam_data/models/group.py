
from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, ConfigDict
from vocal.mixins import VocalGroupMixin

from ..attributes import GroupAttributes
from .dimension import Dimension
from .variable import Variable

class GroupMeta(BaseModel):
    model_config = ConfigDict(
        title='Group Metadata'
    )

    name: str

class Group(BaseModel, VocalGroupMixin):
    model_config = ConfigDict(
        title='Group Schema'
    )

    meta: GroupMeta
    attributes: GroupAttributes
    dimensions: Optional[list[Dimension]] = None
    groups: Optional[list[Group]] = None
    variables: list[Variable]

Group.model_rebuild()
