import datetime
from uuid import UUID
from typing import Optional, Union

from pydantic import  BaseModel, ConfigDict
from vocal.field import Field
from pydantic import model_validator
from vocal.validation import field_validator, substitute_placeholders, is_exact, is_in
from faam_data.validators import validate_conventions


from .constants import *

class GlobalAttributes(BaseModel):

    model_config = ConfigDict(
        title = 'FAAM Global Metadata Schema'
    )

    Conventions: str = Field(
        description="The conventions followed by this data",
        example='CF-1.9 ACDD-1.3 FAAM-0.5'
    )

    acknowledgement: str = Field(
        description=f'The acknowledgement for use of this data. Should read: {ACKNOWLEDGEMENT} for FAAM data.',
        example=ACKNOWLEDGEMENT
    )

    creator_address: str = Field(
        description=f'The address of the FAAM offices. Should read: {CREATOR_ADDRESS} for FAAM data.',
        example=CREATOR_ADDRESS
    )

    creator_email: str = Field(
        description='The email address of the data creator, or a generic FAAM email.',
        example='creator@faam.ac.uk'
    )

    creator_institution: str = Field(
        description=f'The institute responsible for the creation of the data. Should read: {CREATOR_INSTITUTION} for FAAM data',
        example=CREATOR_INSTITUTION
    )

    creator_name: str = Field(
        description='The name of the person or institute responsible for this data',
        example='A. N. Other'
    )

    creator_type: str = Field(
        description=f'The type of creator. Should be one of {", ".join(f'"CREATOR_TYPES"')}',
        example=CREATOR_TYPES[0]
    )

    date: datetime.date = Field(
        description='Date of the flight',
        example='1970-01-01'
    )
    
    date_created: datetime.datetime = Field(
        description='ISO:8601 date/time file created, ideally yyyy-mm-ddTHH:MM:SSZ. Equivalent to revision_date.',
        example='1970-01-01T06:00:00Z'
    )

    flight_date: datetime.date = Field(
        description='Date of the flight',
        example='1970-01-01'
    )

    flight_number: str = Field(
        description='The flight number', pattern='[a-z][0-9]{3}',
        example='a001'
    )

    geospatial_bounds: str = Field(
        description='A well-known text representation of the flight envelope',
        example=''
    )

    geospatial_bounds_crs: str = Field(
        description='Coordinate reference system for geospatial attributes.', pattern='EPSG:[0-9]+',
        example='EPSG:4979'
    )

    geospatial_lat_max: float = Field(
        ge=-90, le=90, description='Maximum latitude of the flight.',
        example=60.0
    )

    geospatial_lat_min: float = Field(
        ge=-90, le=90, description='Minimum latitude of the flight.',
        example=50.0
    )

    geospatial_lat_units: str = Field(
        description='The units for geospatial_lat_* attributes',
        example='degree_north'
    )

    geospatial_lon_max: float = Field(
        description='Maximum longitude of the flight', gt=-360, lt=360,
        example=10.0
    )

    geospatial_lon_min: float = Field(
        description='Minimum longitude of the flight', gt=-360, le=360,
        example=-10.0
    )

    geospatial_lon_units: str = Field(
        description='The units for geospatial_lon_* attributes',
        example='degree_east'  
    )

    geospatial_vertical_max: float = Field(
        description='The maximum altitude of the flight',
        example=10000.0
    )

    geospatial_vertical_min: float = Field(
        description='The minimum altitude of the flight',
        example=100.0
    )

    geospatial_vertical_units: str = Field(
        description='Vertical units associated with geospatial_vertical_* attributes',
        example='m'
    )

    geospatial_vertical_positive: str = Field(
        description='Positive direction of geospatial_vertical_* attributes',
        example='up'
    )

    id: str = Field(
        description='filename without extension, needs to be globally unique w/ naming_authority',
        example='core[-type]_faam_<yyyymmdd>[_vNNN]_rN[_Nhz]'
    )

    institution: str = Field(
        description=f'The institute responsible for the creation of this data. Should read: {CREATOR_INSTITUTION} for FAAM data.',
        example=CREATOR_INSTITUTION
    )

    keywords: str = Field(
        description='A comma separated list of keywords from the GCMD',
        example='keyword1, keyword2'
    )

    keywords_vocabulary: str = Field(
        description=f'Controlled vocabulary for keywords. Should read {KEYWORDS_VOCABULARY}',
        example=KEYWORDS_VOCABULARY
    )

    license: str = Field(
        description=f'The license for this data. Should read: {LICENSE}',
        example=LICENSE
    )

    metadata_link: str = Field(
        description='A link to a release of a controlled vocabulary of metadata attributes',
        example='https://github.com/FAAM-146/faam-data/releases/tag/vX.Y'
    )

    naming_authority: str = Field(
        description=f'The authority responsible for naming this data. Should read {NAMING_AUTHORITY}',
        example=NAMING_AUTHORITY
    )

    platform: str = Field(
        description=f'Platform name of the FAAM aircraft. Should read: {PLATFORM}',
        example=PLATFORM
    )

    platform_type: str = Field(
        description='Platform type: aircraft',
        example=PLATFORM_TYPE
    )

    project: str = Field(
        description='The project a flight was for. Expected to be of the form <project_acronym> - <project_name>',
        example='PROJECT: A project with a long title'
    )

    publisher_email: str = Field(
        description='The email address of the data publisher',
        example='support@ceda.ac.uk'
    )

    publisher_institution: str = Field(
        description=f'The institution responsible for publishing data. Should read: {PUBLISHER_INSTITUTION}',
        example=PUBLISHER_INSTITUTION
    )

    publisher_type: str = Field(
        description=f'Type of entity responsible for publishing data. Should be {PUBLISHER_TYPE}',
        example=PUBLISHER_TYPE
    )

    publisher_url: str = Field(
        description=f'The URL of the data publisher. Should be {PUBLISHER_URL}',
        example=PUBLISHER_URL
    )

    references: str = Field(
        description='A list of references relevant to the file',
        example='https://www.faam.ac.uk https://www.ceda.ac.uk'
    )

    revision_date: Union[datetime.datetime, datetime.date] = Field(
        description='The date this revision created. Analogous to date_created',
        example='1970-01-01T06:00:00Z'
    )

    revision_number: int = Field(
        description='The revision number of the dataset. Starts at 0, increments by 1 for each revision', ge=0,
        example=0
    )

    source: str = Field(
        description='A description of the source of the data. An instrument where this makes sense, otherwise a description of how data obtained',
        example='description of how data obtained'
    )

    standard_name_vocabulary: str = Field(
        description='A vocabulary of standard names. Expected to be a CF standard name table, e.g. CF Standard Name Table v78', pattern='CF Standard Name Table v[0-9]+',
        example='CF Standard Name Table v7'
    )

    summary: str = Field(
        description='A brief summary of the data',
        example='Data obtained on FAAM aircraft during flight a001'
    )

    time_coverage_duration: datetime.timedelta = Field(
        description='The duration of the data, in ISO8601 duration format',
        example='PT1H'
    )

    time_coverage_start: datetime.datetime = Field(
        description='The start time of the data in the file, in ISO8601 format',
        example='1970-01-01T00:00:00Z'
    )

    time_coverage_end: datetime.datetime = Field(
        description='The end time of the data in the file, in ISO8601 format',
        example='1970-01-01T01:00:00Z'
    )

    title: str = Field(
        description='A brief title for the dataset',
        example='Data from flight a001'
    )
    
    uuid: UUID = Field(
        description='V3 UUID: MD5 hash of id+date_created',
        example='9bceaff5-9991-85c6-bca5-d8c0393dc60d'
    )

    # Optional Globals

    calibration_date: Optional[datetime.date] = Field(
        description='Calibration date, where this applies to all file contents',
        example='1970-01-01',
        default=None
    )

    calibration_information: Optional[str] = Field(
        description='Calibration information, where this applies all file contents',
        example='Calibrated at lab X using method Y',
        default=None
    )

    calibration_url: Optional[str] = Field(
        description='Permanent URI or DOI linking to calibration info, where this applies to all file contents',
        example='dx.doi.org/00.0000/0000000',
        default=None
    )

    comment: Optional[str] = Field(
        description='Comment about data',
        example='A comment about the data',
        default=None
    )

    constants_file: Optional[str] = Field(
        description='Name of external file providing input to processing software',
        example='flight-cst_faam_19700101_r0_a001.yaml',
        default=None
    )

    creator_url: Optional[str] = Field(
        description='Institutional URL or researcher ORCID URL',
        example='https://orcid.org/0000-0000-0000-0000',
        default=None
    )

    deployment_mode: Optional[str] = Field(
        description='Mode of deployment. Should always be "air"',
        example='air',
        default=None
    )

    external_variables: Optional[str] = Field(
        description='Blank separated list of variables used from an external file',
        example='PS_RVSM TAT_DI_R',
        default=None
    )

    history: Optional[str] = Field(
        description='Logs modifications to file since production',
        example='1970-01-01T00:00:00Z some_prog -i myfile -o myfile',
        default=None
    )

    instrument: Optional[str] = Field(
        description='Where all data id from a single instrument. Currently freeform, controlled instrument vocab to follow',
        example='Some instrument',
        default=None
    )

    instrument_description: Optional[str] = Field(
        description='Where all data are from a single instrument. Textual description.',
        example='X type instrument, measuring Y using method Z',
        default=None
    )

    instrument_location: Optional[str] = Field(
        description='Where all data are from a single instrument. Location of instrument on aircraft',
        example='Instrument location',
        default=None
    )

    instrument_manufacturer: Optional[str] = Field(
        description='Where all data are from a single instrument. Instrument manufacturer',
        example='Instrument Manufacturing Ltd.',
        default=None
    )

    instrument_model: Optional[str] = Field(
        description='Where all data are from a single instrument. Instrument model',
        example='Model 1.2.3',
        default=None
    )

    instrument_serial_number: Optional[str] = Field(
        description='Where all data are from a single instrument. Instrument serial number',
        example='SN123',
        default=None
    )

    instrument_software: Optional[str] = Field(
        description='Where all data are from a single instrument. Name of software deployed on instrument',
        example='Instrument software name',
        default=None
    )

    instrument_software_version: Optional[str] = Field(
        description='Where all data are from a single instrument. Version of software deployed on instrument',
        example='v1.2.3',
        default=None
    )

    notes: Optional[str] = Field(
        description='Notes on this data file. For more detailed info than comment',
        example='Some longer form notes about this file',
        default=None
    )

    processing_software_commit: Optional[str] = Field(
        description='Commit hash for processing software in vcs',
        example='2a83fc2394b',
        default=None
    )

    processing_software_doi: Optional[str] = Field(
        description='DOI of the processing doftware release, if available',
        example='dx.doi.org/00.0000/0000000',
        default=None
    )

    processing_software_url: Optional[str] = Field(
        description='URL pointing to processing software source code, if available',
        example='https://github.com/my-user/my_repo',
        default=None
    )

    processing_software_version: Optional[str] = Field(
        description='Version of processing software',
        example='v1.2.3',
        default=None
    )

    project_acronym: Optional[str] = Field(
        description='Project acronym',
        example='PROJECT',
        default=None
    )

    project_name: Optional[str] = Field(
        description='Full project name',
        example='A long project name',
        default=None
    )

    project_principal_investigator: Optional[str] = Field(
        description='Name(s) of project PIs. Comma separated if more than one',
        example='A. N. Other',
        default=None
    )

    project_principal_investigator_email: Optional[str] = Field(
        description='Email address(es) of project PIs. Comma separated if more than one',
        example='a.n.other@institute.ac.uk',
        default=None
    )

    project_principal_investigator_url: Optional[str] = Field(
        description='ORCID URL(s) of project PIs. Comma separated if more than one',
        example='https://orcid.org/0000-0000-0000-0000',
        default=None
    )

    revision_comment: Optional[str] = Field(
        description='Brief description of changes between revisions',
        example='Corrected processing of variable X by doing Y',
        default=None
    )

    source_files: Optional[str] = Field(
        description='List of source files used in the processing of this data product',
        example='file1.ext file2.ext',
        default=None
    )

    time_coverage_resolution: Optional[str] = Field(
        description='Resolution of data, where this is uniform across the file',
        example='1S',
        default=None
    )

    processing_level: Optional[str] = Field(
        description='Processing level of data, where it is uniform for all data in the file',
        example=2,
        default=None
    )

    # Allow the use of placeholders, which will be subbed out with examples
    subs_placeholders = model_validator(mode='before')(substitute_placeholders)
    
    _validate_acknowledgement = field_validator('acknowledgement')(is_exact(ACKNOWLEDGEMENT))
    _validate_creator_address = field_validator('creator_address')(is_exact(CREATOR_ADDRESS))
    _validate_creator_institution = field_validator('creator_institution')(is_exact(CREATOR_INSTITUTION))
    _validate_creator_type = field_validator('creator_type')(is_in(CREATOR_TYPES))
    _validate_geospatial_vertical_units = field_validator('geospatial_vertical_units')(is_exact('m'))
    _validate_geospatial_vertical_positive = field_validator('geospatial_vertical_positive')(is_exact('up'))
    _validate_keywords_vocabulary = field_validator('keywords_vocabulary')(is_exact(KEYWORDS_VOCABULARY))
    _validate_license = field_validator('license')(is_exact(LICENSE))
    _validate_naming_authority = field_validator('naming_authority')(is_exact(NAMING_AUTHORITY))
    _validate_platform = field_validator('platform')(is_exact(PLATFORM))
    _validate_platform_type = field_validator('platform_type')(is_exact(PLATFORM_TYPE))
    _validate_publisher_type = field_validator('publisher_type')(is_exact(PUBLISHER_TYPE))
    _validate_publisher_institution = field_validator('publisher_institution')(is_exact(PUBLISHER_INSTITUTION))
    _validate_publisher_url = field_validator('publisher_url')(is_exact(PUBLISHER_URL))
    _validate_conventions = field_validator('Conventions')(validate_conventions)
    