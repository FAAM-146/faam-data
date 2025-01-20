import datetime

from typing import Optional, Union

from pydantic import  BaseModel, model_validator, ConfigDict
from vocal.field import Field
from vocal.types import Numeric, int32
from vocal.validation import substitute_placeholders, in_vocabulary, validate, Attribute
from vocal.vocab import CFStandardNames
from vocal.mixins import VocalAttributesMixin

from faam_data.vocabularies import CoverageContentTypes
from faam_data.validators import validate_units, validate_units_compatible_with_name

from .constants import *


CF_STANDARD_NAMES = CFStandardNames(version=88)


class VariableAttributes(BaseModel, VocalAttributesMixin):
    model_config = ConfigDict(
        # Configuration options here
        title = 'Variable Attributes',
        populate_by_name = True,
        arbitrary_types_allowed = True
    )

    FillValue: Union[int, float] = Field(
        description='The prefill/missing data value',
        alias='_FillValue',
        example=-9999, ppodd_default=-9999
    )

    coverage_content_type: str = Field(
        description=f'ISO 19115-1 code. One of {", ".join(COVERAGE_CONTENT_TYPES)}',
        example=COVERAGE_CONTENT_TYPES[2], ppodd_default='physicalMeasurement'
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
        example='X',
        default=None
    )

    actual_range: Optional[list[Numeric]] = Field(
        description='A length 2 array, of the same datatype as the variable, giving the maximum and minimum valid values',
        example=[0, 1],
        ppodd_default='<call range>',
        default=None
    )

    add_offset: Optional[Numeric] = Field(
        description='Offset for packing. Default is 0',
        example=0,
        default=None
    )

    ancillary_variables: Optional[str] = Field(
        description='Optional in no ancillary variables, otherwise required. Ancillary variables e.g. flags, uncertainties',
        example='PS_RVSM TAT_DI_R',
        default=None
    )

    calendar: Optional[str] = Field(
        description=f'Required for the time coordinate variable. Should be one of {", ".join(ALLOWED_CALENDARS)}',
        example=ALLOWED_CALENDARS[0],
        default=None
    )

    calibration_date: Optional[datetime.date] = Field(
        description='Calibration date, where this applies to variable',
        example='1970-01-01',
        default=None
    )

    calibration_information: Optional[str] = Field(
        description='Calibration information, where this applies variable',
        example='Calibrated at lab X using method Y',
        default=None
    )

    calibration_url: Optional[str] = Field(
        description='Permanent URI or DOI linking to calibration info, where this applies to variable',
        example='dx.doi.org/00.0000/0000000',
        default=None
    )

    comment: Optional[str] = Field(
        description='Comment about data',
        example='A comment about the data',
        default=None
    )

    coordinates: Optional[str] = Field(
        description='Blank separated list of coordinate variables',
        example='latitude longitude altitude time',
        default=None
    )

    flag_masks: Optional[Union[list[int], int]] = Field(
        description='Allowed flag mask values. Required for bitmask style flags',
        example=[1, 2, 4],
        default=None
    )

    flag_meanings: Optional[str] = Field(
        description='Blank separated list of flag meanings. Required for flag variables',
        example='data_good possible_minor_issue possible_major_issue',
        default=None
    )

    flag_values: Optional[Union[list[int], int]] = Field(
        description='Allowed flag values. Required for classic flags',
        example=[0, 1, 2],
        default=None
    )

    frequency: Optional[int32] = Field(
        description=(
            'The frequency of the data, when it is of uniform frequency. '
            'This attribute should be given whenever the data is of uniform frequency, and '
            'must be given when using an "sps" dimension.'
        ),
        example=1,
        default=None
    )

    instrument_description: Optional[str] = Field(
        description='Textual description of instrument.',
        example='X type instrument, measuring Y using method Z',
        default=None
    )

    instrument_location: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Location of instrument on aircraft',
        example='Instrument location',
        default=None
    )

    instrument_manufacturer: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Instrument manufacturer',
        example='Instrument Manufacturing Ltd.',
        default=None
    )

    instrument_model: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Instrument model number',
        example='Model 1.2.3',
        default=None
    )

    instrument_serial_number: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Instrument serial number',
        example='SN123',
        default=None
    )

    instrument_software: Optional[str] = Field(
        description='Where variable is derived from a single instrument. Name of software deploed on instrument',
        example='Instrument software name',
        default=None
    )

    instrument_software_version: Optional[str] = Field(
        description='Where all data in the group are from a single instrument. Version of software deployed on instrument',
        example='v1.2.3',
        default=None
    )

    sensor_manufacturer: Optional[str] = Field(
        description='Similar to instrument_manufacturer, but where the item is more accurately described as a sensor',
        example='Sensor Manufacturing Ltd.',
        default=None
    )

    sensor_model: Optional[str] = Field(
        description='Similar to instrument_model, but where the item is more accurately described as a sensor',
        example='Model 1.2.3',
        default=None
    )

    sensor_serial_number: Optional[str] = Field(
        description='Where variable is derived from a single sensor, similar to instrument_serial_number. Sensor serial number.',
        example='SN123',
        default=None
    )

    sensor_type: Optional[str] = Field(
        description=('The type of sensor fitted, where different sensor types may be used to produce the same measurement. '
                     'A canonical example of this is the type of temperature sensor in the Rosemount housings.'),
        example='plate',
        default=None
    )

    positive: Optional[str] = Field(
        description='Applies to vertical coordinate. Should be "up" if included',
        example='up',
        default=None
    )

    scale_factor: Optional[Numeric] = Field(
        description='Scale for packing. Default is 1',
        example=1,
        default=None
    )

    standard_name: Optional[str] = Field(
        description='See CF standard names list. Should be used whenever possible',
        example='air_temperature',
        default=None
    )

    valid_max: Optional[Numeric] = Field(
        description='Recommended where feasible. Where both valid_min and valid_max make sense, valid_range is preferred.',
        example=1,
        default=None
    )

    valid_min: Optional[Numeric] = Field(
        description='Recommended where feasible. Where both valid_min and valid_max make sense, valid_range is preferred.',
        example=0,
        default=None
    )

    valid_range: Optional[list[Numeric]] = Field(
        description='A length 2 array of the same datatype as the variable, giving minimum and maximum valid values', min_items=2, max_items=2,
        example=[0, 1],
        default=None
    )

    processing_level: Optional[str] = Field(
        description='Processing level of variable data',
        example='2',
        default=None
    )

    # Allow the use of placeholders, which will be subbed out with examples
    subs_placeholders = model_validator(mode='before')(substitute_placeholders)
    
    # Validate the standard_name against the CF standard names vocabulary
    _validate_standard_name = validate(
        Attribute('standard_name'),
        in_vocabulary(CF_STANDARD_NAMES)
    )

    # Validate the coverage_content_type against the CoverageContentTypes vocabulary
    _validate_coverage_content_type = validate(
        Attribute('coverage_content_type'), 
        in_vocabulary(CoverageContentTypes())
    )

    # Validate units
    _validate_units = validate_units

    # Validate that units are compatible with standard name
    _validate_units_compatible_with_name = validate_units_compatible_with_name
