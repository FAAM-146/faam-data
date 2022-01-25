
from pydantic import Field, BaseModel

class GroupAttributes(BaseModel):
    class Config:
        # Configuration options here
        title = 'Group Attributes'

    # Add your attributes here, e.g.
    #
    # my_attribute: str = Field(
    #   description='A description of my attribute',
    #   example='my_attribute_value'
    # )
