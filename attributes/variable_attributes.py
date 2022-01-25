
from pydantic import Field, BaseModel

class VariableAttributes(BaseModel):
    class Config:
        # Configuration options here
        title = 'Variable Attributes'

    # Add your attributes here, e.g.
    #
    # my_attribute: str = Field(
    #   description='A description of my attribute',
    #   example='my_attribute_value'
    # )
