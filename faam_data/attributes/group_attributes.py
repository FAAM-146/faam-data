from typing import Optional
import datetime

from pydantic import BaseModel, model_validator, ConfigDict
from vocal.field import Field
from vocal.validation import substitute_placeholders
from vocal.mixins import VocalAttributesMixin

class GroupAttributes(BaseModel, VocalAttributesMixin):
    model_config = ConfigDict(
        # Configuration options here
        title = 'FAAM Group Attributes'
    )

    calibration_date: Optional[datetime.date] = Field(
        description='Calibration date, where this applies to whole group',
        example='1970-01-01',
        default=None
    )

    calibration_information: Optional[str] = Field(
        description='Calibration information, where this applies whole group',
        example='Calibrated at lab X using method Y',
        default=None
    )

    calibration_url: Optional[str] = Field(
        description='Permanent URI or DOI linking to calibration info, where this applies to whole group',
        example='dx.doi.org/00.0000/0000000',
        default=None
    )

    comment: Optional[str] = Field(
        description='Comment about data',
        example='A comment about the data',
        default=None
    )

    instrument: Optional[str] = Field(
        description='Currently freeform, controlled instrument vocab to follow',
        example='Some instrument',
        default=None
    )

    instrument_description: Optional[str] = Field(
        description='Textual description.',
        example='X type instrument, measuring Y using method Z',
        default=None
    )

    instrument_location: Optional[str] = Field(
        description='Location of instrument on aircraft',
        example='Instrument location',
        default=None
    )

    instrument_manufacturer: Optional[str] = Field(
        description='Instrument manufacturer',
        example='Instrument Manufacturing Ltd.',
        default=None
    )

    instrument_model: Optional[str] = Field(
        description='Instrument model',
        example='Model 1.2.3',
        default=None
    )

    instrument_serial_number: Optional[str] = Field(
        description='Instrument serial number',
        example='SN123',
        default=None
    )

    instrument_software: Optional[str] = Field(
        description='Name of softeare deployed on instrument',
        example='Instrument software name',
        default=None
    )

    instrument_software_version: Optional[str] = Field(
        description='Version of software deployed on instrument',
        example='v1.2.3',
        default=None
    )
    
    notes: Optional[str] = Field(
        description='Notes on this group. For more detailed info than comment',
        example='Some longer form notes about this file',
        default=None
    )

    source_files: Optional[str] = Field(
        description='List of source files used in the processing of this group',
        example='file1.ext file2.ext',
        default=None
    )

    references: Optional[str] = Field(
        description='A list of references relevant to the group',
        example='https://www.faam.ac.uk https://www.ceda.ac.uk',
        default=None
    )

    processing_level: Optional[str] = Field(
        description='Processing level of data, where it is uniform for all data in the group',
        example='2',
        default=None
    )

    source: Optional[str] = Field(
        description='A description of the source of the data. An instrument where this makes sense, otherwise a description of how data obtained',
        example='description of how data obtained',
        default=None
    )

    summary: Optional[str] = Field(
        description='A brief summary of the data',
        example='Data obtained on FAAM aircraft during flight a001',
        default=None
    )

    # Allow the use of placeholders, which will be subbed out with examples
    subs_placeholders = model_validator(mode='before')(substitute_placeholders)