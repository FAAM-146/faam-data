from pydantic import BaseModel, model_validator
from typing import List

from vocal.field import Field
from vocal.mixins import VocalVariableMixin
from ..attributes import VariableAttributes


class VariableMeta(BaseModel):
    datatype: str = Field(description="The type of the data")
    name: str
    required: bool = True


class Variable(BaseModel, VocalVariableMixin):
    meta: VariableMeta
    dimensions: List[str]
    attributes: VariableAttributes

    @model_validator(mode="after")
    @classmethod
    def validate_frequency(cls, v):
        frequency = v.attributes.frequency
        has_sps_dim = any([d.startswith("sps") for d in v.dimensions])
        if frequency is None and has_sps_dim:
            raise ValueError(
                '"frequency" attribute is required when using sps dimension'
            )
        return v
