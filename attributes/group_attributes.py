from typing import Optional
import datetime

from pydantic import Field, BaseModel, root_validator
from vocal.validation import substitute_placeholders

class GroupAttributes(BaseModel):
    class Config:
        # Configuration options here
        title = 'FAAM Group Attributes'

    calibration_date: Optional[datetime.date] = Field(
        description='Calibration date, where this applies to whole group',
        example='1970-01-01'
    )

    calibration_information: Optional[str] = Field(
        description='Calibration information, where this applies whole group',
        example='Calibrated at lab X using method Y'
    )

    calibration_url: Optional[str] = Field(
        description='Permanent URI or DOI linking to calibration info, where this applies to whole group',
        example='dx.doi.org/00.0000/0000000'
    )

    comment: Optional[str] = Field(
        description='Comment about data',
        example='A comment about the data'
    )

    instrument: Optional[str] = Field(
        description='Currently freeform, controlled instrument vocab to follow',
        example='Some instrument'
    )

    instrument_description: Optional[str] = Field(
        description='Textual description.',
        example='X type instrument, measuring Y using method Z'
    )

    instrument_location: Optional[str] = Field(
        description='Location of instrument on aircraft',
        example='Instrument location'
    )

    instrument_manufacturer: Optional[str] = Field(
        description='Instrument manufacturer',
        example='Instrument Manufacturing Ltd.'
    )

    instrument_model: Optional[str] = Field(
        description='Instrument model',
        example='Model 1.2.3'
    )

    instrument_serial_number: Optional[str] = Field(
        description='Instrument serial number',
        example='SN123'
    )

    instrument_software: Optional[str] = Field(
        description='Name of softeare deployed on instrument',
        example='Instrument software name'
    )

    instrument_software_version: Optional[str] = Field(
        description='Version of software deployed on instrument',
        example='v1.2.3'
    )
    
    notes: Optional[str] = Field(
        description='Notes on this group. For more detailed info than comment',
        example='Some longer form notes about this file'
    )

    source_files: Optional[str] = Field(
        description='List of source files used in the processing of this group',
        example='file1.ext file2.ext'
    )

    references: Optional[str] = Field(
        description='A list of references relevant to the group',
        example='https://www.faam.ac.uk https://www.ceda.ac.uk'
    )

    processing_level: Optional[str] = Field(
        description='Processing level of data, where it is uniform for all data in the group',
        example='2'
    )

    source: Optional[str] = Field(
        description='A description of the source of the data. An instrument where this makes sense, otherwise a description of how data obtained',
        example='description of how data obtained'
    )

    summary: Optional[str] = Field(
        description='A brief summary of the data',
        example='Data obtained on FAAM aircraft during flight a001'
    )

    # Allow the use of placeholders, which will be subbed out with examples
    subs_placeholders = root_validator(pre=True, allow_reuse=True)(substitute_placeholders)