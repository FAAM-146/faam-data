============
Introduction
============

This document describes the netCDF metadata attributes which are
associated with compliant FAAM datasets. Metadata attributes are 
specified as global, group, or variable level, and are either
optional or required for compliance.

General Guidance
----------------

* Dates and datetimes should be provided in ISO 8601 format, and 
  should be given in UTC where possible. Preferred formats are:

  * ``yyyy-mm-ddTHH:MM:SSZ`` for datetimes
  * ``yyyy-mm-dd`` for dates