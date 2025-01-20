==============================
Attribute Metadata Conventions
==============================

------------
Introduction
------------

This section describes the netCDF metadata attributes which are
associated with compliant FAAM datasets. Metadata attributes are 
specified as global, group, or variable level, and are either
optional or required for compliance.

General Guidance
----------------

* Dates and datetimes should be provided in ISO 8601 format, and 
  should be given in UTC where possible. Preferred formats are:

  * ``yyyy-mm-ddTHH:MM:SSZ`` for datetimes
  * ``yyyy-mm-dd`` for dates

-----------------
Global Attributes
-----------------

Required Global Attributes
--------------------------

TAG_REQUIRED_GLOBAL_ATTRIBUTES

Optional Global Attributes
--------------------------

TAG_OPTIONAL_GLOBAL_ATTRIBUTES

Validations
-----------

TAG_GLOBAL_ATTRIBUTE_VALIDATIONS

----------------
Group Attributes
----------------

Required Group Attributes
--------------------------

TAG_REQUIRED_GROUP_ATTRIBUTES

Optional Group Attributes
-------------------------

TAG_OPTIONAL_GROUP_ATTRIBUTES

Validations
-----------

TAG_GROUP_ATTRIBUTE_VALIDATIONS

-------------------
Variable Attributes
-------------------

Required Variable Attributes
----------------------------

TAG_REQUIRED_VARIABLE_ATTRIBUTES

Optional Variable Attributes
----------------------------

TAG_OPTIONAL_VARIABLE_ATTRIBUTES

Validations
-----------

TAG_VARIABLE_ATTRIBUTE_VALIDATIONS

