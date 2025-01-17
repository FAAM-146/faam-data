from pydantic import BaseModel
from typing import List

from vocal.field import Field
from vocal.mixins import VocalVariableMixin
from faam_data.validators import validate_frequency
from ..attributes import VariableAttributes


class VariableMeta(BaseModel):
    datatype: str = Field(description="The type of the data")
    name: str
    required: bool = True


class Variable(BaseModel, VocalVariableMixin):
    meta: VariableMeta
    dimensions: List[str]
    attributes: VariableAttributes

    _validate_frequency = validate_frequency
