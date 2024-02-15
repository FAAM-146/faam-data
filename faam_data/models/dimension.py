
from pydantic import BaseModel
from typing import Union

from vocal.mixins import VocalDimensionMixin

class Dimension(BaseModel, VocalDimensionMixin):
    name: str
    size: Union[int, None]
