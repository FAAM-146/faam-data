import datetime

from typing import Optional, Union

from pydantic import Field, BaseModel, root_validator
from vocal.schema_types import Numeric
from vocal.validation import substitute_placeholders

from .constants import *

class VariableAttributes(BaseModel):
    class Config:
        # Configuration options here
        title = 'Variable Attributes'
        allow_population_by_field_name=True

    FillValue: Union[int, float] = Field(
        description='The prefill/missing data value',
        alias='_FillValue',
        example=-9999, ppodd_default=-9999
    )

    coverage_content_type: str = Field(
        description=f'ISO 19115-1 code. One of {", ".join(COVERAGE_CONTENT_TYPES)}',
        example=COVERAGE_CONTENT_TYPES[2], ppodd_default='physicalMeasurement'
    )

    frequency: int = Field(
        description='The frequency of the data. Where this is >1, will typically correspond to an spsNN dimension',
        example=1
    )

    long_name: str = Field(
        description='A longer, descriptive name for the variable',
        example='Temperature from deiced temperature probe'
    )

    units: str = Field(
        description='Valid UDUNITS unit. Where a standard_name is given, must be equivalent to canonical units',
        example='K'
    )

    # Optional Attributes
    axis: Optional[str] = Field(
        description=f'Axis for coordinate variables. Should be one of {", ".join(AXIS_TYPES)}',
        example='X'
    )

    actual_range: Optional[list[Numeric]] = Field(
        description='A length 2 array, of the same datatype as the variable, giving the maximum and minimum valid values',
        example=[0, 1],
        ppodd_default='<call range>'
    )

    add_offset: Optional[Numeric] = Field(
        description='Offset for packing. Default is 0',
        example=0
    )

    ancillary_variables: Optional[str] = Field(
        description='Optional in no ancillary variables, otherwise required. Ancillary variables e.g. flags, uncertainties',
        example='PS_RVSM TAT_DI_R'
    )

    calendar: Optional[str] = Field(
        description=f'Required for the time coordinate variable. Should be one of {", ".join(ALLOWED_CALENDARS)}',
        exmaple=ALLOWED_CALENDARS[0]
    )

    calibration_date: Optional[datetime.date] = Field(
        description='Calibration date, where this applies to variable',
        example='1970-01-01'
    )

    calibration_information: Optional[str] = Field(
        description='Calibration information, where this applies variable',
        example='Calibrated at lab X using method Y'
    )

    calibration_url: Optional[str] = Field(
        description='Permanent URI or DOI linking to calibration info, where this applies to variable',
        example='dx.doi.org/00.0000/0000000'
    )

    comment: Optional[str] = Field(
        description='Comment about data',
        example='A comment about the data'
    )

    coordinates: Optional[str] = Field(
        description='Blank separated list of coordinate variables',
        example='latitude longitude altitude time'
    )

    flag_masks: Optional[Union[list[int], int]] = Field(
        description='Allowed flag mask values. Required for bitmask style flags',
        example=[1, 2, 4]
    )

    flag_meanings: Optional[str] = Field(
        description='Blank separated list of flag meanings. Required for flag variables',
        example='data_good possible_minor_issue possible_major_issue'
    )

    flag_values: Optional[Union[list[int], int]] = Field(
        description='Allowed flag values. Required for classic flags',
        example=[0, 1, 2]
    )

    instrument_description: Optional[str] = Field(
        description='Textual description of instrument.',
        example='X type instrument, measuring Y using method Z'
    )

    instrument_location: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Location of instrument on aircraft',
        example='Instrument location'
    )

    instrument_manufacturer: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Instrument manufacturer',
        example='Instrument Manufacturing Ltd.'
    )

    instrument_model: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Instrument model number',
        example='Model 1.2.3'
    )

    instrument_serial_number: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Instrument serial number',
        example='SN123'
    )

    instrument_software: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Name of software deploed on instrument',
        example='Instrument software name'
    )

    instrument_software_version: Optional[str] = Field(
        description='Where all data in the group are from a single instrument. Version of software deployed on instrument',
        example='v1.2.3'
    )

    sensor_manufacturer: Optional[str] = Field(
        description='Similar to instrument_manufacturer, but where the item is more accurately described as a sensor',
        example='Sensor Manufacturing Ltd.'
    )

    sensor_model: Optional[str] = Field(
        description='Similar to instrument_model, but where the item is more accurately described as a sensor',
        example='Model 1.2.3'
    )

    sensor_serial_number: Optional[str] = Field(
        description='Where variable is derived from a single sensor, similar to instrument_serial_number. Sensor serial number.',
        example='SN123'
    )

    sensor_type: Optional[str] = Field(
        description=('The type of sensor fitted, where different sensor types may be used to produce the same measurement. '
                     'A canonical example of this is the type of temperature sensor in the Rosemount housings.'),
        example='plate'
    )

    positive: Optional[str] = Field(
        description='Applies to vertical coordinate. Should be "up" if included',
        example='up'
    )

    scale_factor: Optional[Numeric] = Field(
        description='Scale for packing. Default is 1',
        example=1
    )

    standard_name: Optional[str] = Field(
        description='See CF standard names list. Should be used whenever possible',
        example='air_temperature'
    )

    valid_max: Optional[Numeric] = Field(
        description='Recommended where feasible. Where both valid_min and valid_max make sense, valid_range is preferred.',
        example=1
    )

    valid_min: Optional[Numeric] = Field(
        description='Recommended where feasible. Where both valid_min and valid_max make sense, valid_range is preferred.',
        example=0
    )

    valid_range: Optional[list[Numeric]] = Field(
        description='A length 2 array of the same datatype as the variable, giving minimum and maximum valid values', min_items=2, max_items=2,
        example=[0, 1]
    )

    processing_level: Optional[str] = Field(
        description='Processing level of variable data',
        example='2'
    )

    # Allow the use of placeholders, which will be subbed out with examples
    subs_placeholders = root_validator(pre=True, allow_reuse=True)(substitute_placeholders)
    

