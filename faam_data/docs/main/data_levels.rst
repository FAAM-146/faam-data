======================
Data Processing Levels
======================

Data processing levels are defined as as attribute called `processing_level`. 
This attribute is defined in `ACDD-1.3`` as a global variable. FAAM recommend 
this be applied at the variable level unless all variables in a file or group 
share the same processing level, in which case it may be applied at the global 
or group level.

-----------------
Processing Levels
-----------------

Level 0-0
---------

Unadulterated raw instrument data in the native instrument format. File/s may 
be compressed and/or combined with level 0-0 data from other instruments or 
time periods.

Level 0-1
---------

Unprocessed instrument data at original resolution. Data may be flagged to 
designate data artefacts, calibration periods, pre- and post-flight tails, etc. 
Duplicates or exceptional empty data may be removed. Data may be converted to a 
different file format and metadata added. Automatic quality control may be 
applied.

Level 1A
--------

Data variable derived from a single level 0 or 1A data product. An Automatic 
level of quality control has been applied to the process inputs and/or the 
derived output.

Level 1B
--------

Data variable derived from multiple level 0 or 1A data products. An Automatic 
level of quality control has been applied to the process inputs and/or the 
derived output.

Level 2A
--------

Level 1A data that has been irreversibly transformed through changes to the 
dimensions. This may include temporal changes through interpolation, averaging, 
or sub-sampling or spatial changes by aligning to a regularised geophysical 
coordinate (latitude, longitude and altitude). An Automatic level of quality 
control has been applied.

Level 2B
--------

Level 1B data that has been irreversibly transformed through changes to the 
dimensions. This may include temporal changes through interpolation, averaging, 
or sub-sampling or spatial changes by aligning to a regularised geophysical 
coordinate (latitude, longitude and altitude). An Automatic level of quality 
control has been applied.

Level 3A
--------

Level 1A or 2A data that has undergone a Standard level of quality control.

Level 3B
--------

Level 1B or 2B data that has undergone a Standard level of quality control.

Level 4
-------

Level 4 data is derived from Level 3A or 3B data spanning an extended period of 
time or from different platforms. For example, this may be derived from data 
from an entire campaign or collected over many flights or from multiple aircraft 
and/or ground sites. Level 4 data requires a Comprehensive level of quality 
control.

----------------------
Quality Control levels
----------------------

Automatic
---------

Data quality is characterised based on instrument operating envelope, for 
example acceptable probe internal temperature; platform state, for example 
whether the aircraft is in the air or on the ground; or data values, for 
example negative data when this is not physically possible. This level of 
quality control is done automatically during processing based on a series of 
data- or instrument-specific criteria.


Standard
--------

Data is checked based on the reasonableness of the physical quantity being 
measured at the time it is measured. Where possible, data are cross referenced 
with comparable or complementary physical variables from the same flight. For 
example, the static pressure may be checked against the aircraft measurement of 
the same property as well as being within some range of the standard atmosphere 
pressure given the altitude derived from the GIN. This level of quality control
may be carried out automatically in the processing code or may require human 
intervention and manual flagging. At this level Automatic quality control is 
implied.


Comprehensive
-------------

An in-depth evaluation of data quality has been undertaken by an expert. 
This may include quantitative analysis of instrument state and behaviour over 
multiple flights. Manual QC flags are applied where data are found to be of 
degraded quality. At this level Standard quality control is implied.

