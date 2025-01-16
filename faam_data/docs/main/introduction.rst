============
Introduction
============

-------
Summary
-------

This document provides a description of the FAAM data standard, and the data 
products known to be compliant with it. Data products may identify themselves
as being compliant with this standard through the use of the ``metadata_link``
ACDD attribute, which should point to a release of the ``faam-data`` repository,
or though identifying with the FAAM-x.y conventions in the netCDF ``Conventions`` attribute, where the ``x.y`` corresponds to the metadata
release.

---------------
FAIR Principles
---------------

Data provided by FAAM are intended to follow the FAIR principles, introduced by Wilkinson et al., 2016 (http://dx.doi.org/10.1038/sdata.2016.18). FAIR means that the data are **F**\ indable, **A**\ cessible, **I**\ nteroperable and **R**\ eusable. A full description of the FAIR principles is available at https://go-fair.org/fair-principles/. For convenience, these are reproduced in part below.

Findable
--------

The first step in (re)using data is to find them. Metadata and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services, so this is an essential component of the FAIRification process.

* (Meta)data should be assigned a globally unique and persistent identifier.
* Data should be described with rich metadata.
* Metadata should clearly and explicitly include the identifier of the data they describe.
* (Meta)data are registered or indexed in a searchable resource.

Accessible
----------

Once the user finds the required data, she/he needs to know how can they be accessed, possibly including authentication and authorisation.

* (Meta)data should be retreivable by their identifier using a standardised communications protocol
    * The protocol should be open, free, and universally implementable.
    * The protocol should allow for an authentication and authorisation procedure, where necessary.
* Metadata should be accessible, even when the data are no longer available.

Interoperable
-------------

The data usually need to be integrated with other data. In addition, the data need to interoperate with applications or workflows for analysis, storage, and processing.

* (Meta)data should use a formal, accessible, shared, and broadly applicable language for knowledge representation.
* (Meta)data should use vocabularies that follow FAIR principles.
* (Meta)data should include qualified references to other (meta)data.

Reusable
--------

The ultimate goal of FAIR is to optimise the reuse of data. To achieve this, metadata and data should be well-described so that they can be replicated and/or combined in different settings.

* (Meta)data should be richly described with a plurality of accurate and relevant attributes.
    * (Meta)data should be released with a clear and accessible data usage license.
    * (Meta)data should be associated with detailed provenance.
    * (Meta)data should meet domain-relevant community standards.

------
NetCDF
------

The FAAM core data product is provided in the **netCDF** format. NetCDF (Network Common Data Form) is a set of software libraries and platform independent data formats which are designed to support the creation, access, and sharing of array-oriented scientific data. NetCDF is designed to be

* **Self-describing.** A netCDF file includes information about the data it contains (i.e. metadata).
* **Portable.** A netCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.
* **Scalable.** A small subset of a large dataset may be accessed efficiently.
* **Appendable.** Data may be appended to a properly structured netCDF file without copying the dataset or redefining its structure.
* **Shareable.** One writer and many readers may simultaneously access the same netCDF file.
* **Archivable.** Access to all earlier forms of netCDF data will be supported by current and future versions of the software.

NetCDF is extremely commonly used, and is almost ubiquitous within the Earth sciences. Unidata (https://unidata.ucar.edu) provide and maintain software libraries for accessing netCDF data using C, C++, Java, and FORTRAN. Third-party libraries (which are generally bindings or wrappers to the Unidata libraries) are available for Python, IDL, MATLAB, R, Ruby, and Perl, among others.

NetCDF files generally consist of four components:

* **Attributes.** Attributes are metadata which can be attached to the netCDF file itself (called global attributes), to variables, and to groups (variable attributes and groups attributes, respectively). Attributes may be textual or numeric; numeric attributes may be arrays.
* **Groups.** Groups (available since netCDF4) provide a method to encapsulate related *dimensions,* *variables,* and *attributes.* They can be thought of as somewhat analogous to directories in a filesystem.
* **Dimensions.** Dimensions specify the size of a single axis of a variable within a netCDF file. Common dimensions for geophysical data include time, latitude, and longitude, though they do not need to correspond to physical dimensions. There is no practical limit to the number of dimensions which may be defined in a netCDF file.
* **Variables.** Variables are named *n*\ -dimensional (thus associated with *n* *dimensions*) arrays of a specified data type. Variables may have zero or more *attributes*, which act as metadata to describe the contents of the variable. Zero dimensional variables may be referred to as *scalar* variables.

A minimal example of accessing a 1-dimensional variable, *data*, along with its *units* attribute and a global *title* attribute from a netCDF file, using python, is given below. Note that the netCDF library, *netCDF4*, is not included as part of the python standard library, but may be installed using your system package manager, pip, or conda.

.. code-block:: python
    :linenos:

    from netCDF4 import Dataset

    with Dataset('somefile.nc', 'r') as nc:
        title = nc.title
        data_units = nc['data'].units
        data_data = nc['data'][:]

Python software libraries to aid in accessing FAAM data are in development, and will be made available in due course.

-------------
NCAS-Airborne
-------------

FAAM's data has made use of the NetCDF file format since the facility's inception in 2004, in common with approaches taken on similar aircraft platforms globally.

Several factors continue to govern choices of how the FAAM data are represented within what has become known as the NCAS-Airborne standard:

* Early users developed applications to easily view all available data from their (and other) airborne facilities. These were typically user-interactive, and it made sense for the data to be grouped into a small number of files to enable its simple use with tools like these.
* FAAM users wanted, as far as possible, all the data in one file. In many cases data analysis or correction schemes rely on not just a single parameter, and the dependent variables for a given experiment cannot be assumed to always be time, position, or altitude. An alternative approach, to reproduce data files per-instrument with a small number of key dependent variables alongside individual parameters, would have resulted in inefficient use of storage - typically 50+ instrument systems support the main FAAM dataset for a flight.
* There is no single source of truth for some measurements, because of different performance characteristics. Data from different sources are therefore presented together to facilitate this choice being made by a user.
* Other international airborne facilities pursued the same approach, and FAAM seeks to retain commonality as far as possible with their user communities, enabling code to be shared and re-used.

Timeseries Packing
------------------

One of the major differences between the FAAM data standard (following the RAL conventions) and the
other NCAS data standards is the use of timseseries packing. This is where timeseries data at a
frequence above 1 Hz are packed into a 2-dimensional array, with the first dimension being a 1 Hz
representation of time, and the second dimension being the number of samples in each second.

For example, a timeseries of 10 Hz data spanning 5 seconds would be packed into a 2D array of shape
(5, 10). The first dimension should correspond to the 1 Hz time dimension, and the second dimension
should correspond to the number of samples in each second. When packed like this, the second
dimension should be named `spsNN`, where `NN` is a two-digit number representing the number of samples
in each second, in this case `sps10`.

--------------------
External Conventions
--------------------

This standard relies heavily on the `Climate Forecast (CF) <https://cfconventions.org/>`_ 
comventions and the `Attribute Conventions for Data Discovery (ACDD) <https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3>`_. 
Data which are compliant with this standard should also comply with ``CF-[1.9<=x.y<2.0]`` and 
``ACDD-1.3``. 

CF standard names should be used wherever possible. No particular release of the CF standard
names table is required, however the release used should be specified in the 
``standard_name_vocabulary`` metadata attribute. When checking for compliance, version 88
of the CF standard names table is currently used.

A comma-separated list of keywords should be provided for each data product in the 
``keywords`` metadata attribute. These should be derived from the 
`Global Master Change Directory (GCMD) <https://earthdata.nasa.gov/earth-observation-data/find-data/idn/gcmd-keywords>`_
vocabulary, and this should be noted in the ``keywords_vocabulary`` metadata attribute.

-------------------
Standard Versioning
-------------------

This standard has major and minor versions, which are incremented using the following rules:

* Major version: Incremented when a change is made that is not backwards compatible. This includes:

    * The introdiction of a new required metadata attribute
    * Changing an existing required metadata attribute in a way that would require a change to the data file
    * Changing an optonal metadata attribute in a way that would require a change to the data file
    * Making an optonal metadata attribute required

* Minor version: Incremented when a change is made that is backwards compatible. This includes:

    * Adding a new optional metadata attribute
    * Changing an existing optional metadata attribute in a way that would not require a change to the data file
    * Making a required metadata attribute optional

.. warning::
    
    A major version of 0 indicates pre-release. At version 0.x, breaking changes may be made 
    without incrementing the major version.

-------------------
Compliance Checking
-------------------

FAAM use standard and product definitons in a format understood by the
`Vocal <https://github.com/FAAM-146/vocal>`_ tool. This tool can be used to:

* Check that a file is compliant with the standard and product definitions
* Create 'example' netCDF files that are compliant with the standard and product definitions
* Create empty netCDF files for a given product definition which the data producer can populate

The tool is available as a python package, and can be installed using pip:

.. code-block:: bash

    pip install git+https://github.com/FAAM-146/vocal.git

Files may then be checked against the project and product definitions provided in the `faam-data` repository
found at https://github.com/FAAM-146/faam-data. For example:

.. code-block:: bash

    vocal check --project $PWD/faam-data/faam_data --definition $PWD/faam-data/products/latest/my_product_definition.json my_file.nc

Alternatively the latest release of the standard and product definitions can be downloaded and
installed locally using `vocal`, to simplify the process:

.. code-block:: bash

    vocal fetch https://github.com/faam-146/faam-data

Then the check command can be run without specifying the project and definition:

.. code-block:: bash

    vocal check my_file.nc

This will work as long as the file declares the standard in the ``Conventions`` attribute, for example:
``Conventions: "CF-1.6 ACDD-1.3 FAAM-0.4"``.

`Vocal` also offers a basic web interface, which can be started using:

.. code-block:: bash

    vocal web

A full description of *vocal* and its use can be found at the `GitHub repository <https://github.com/FAAM-146/vocal>`_.
Usage help on the command line can be found by running:

.. code-block:: bash

    vocal help

or 

.. code-block:: bash

    vocal <command> -h

------------------------------
Citable Documentation and Code
------------------------------

FAAM use `Zenodo <https://zenodo.org>`_ to provide `Digital Object Identifiers (DOIs) <https://doi.org>`_ to documentation, processing code, and calibration information. DOIs provide persistent identifiers to digital assets, and may be used to reference information in journal publications.

FAAM assets can be found through the `FAAM Community Portal <https://zenodo.org/communities/faam-146>`_ on Zenodo.

------------------------
Data access and archival
------------------------

FAAM aim to process and make available a preliminary version of the core (DECADES)
data product within 24 hours of a flight, although this may take slightly longer
when on detachment. The preliminary DECADES file, indicated by the postfix
``_prelim`` in the filename will initially be made available to registered users
through the `FAAM website <https://www.faam.ac.uk>`_, where it will also be available to visualise.

The preliminary file is intended to be used only for initial visualisation and
analysis while the data go through inspection and manual flagging.

Once all of the variables in this file have been checked by a FAAM staff member,
the data will be archived at the Centre for Environmental Data Analysis
(CEDA; https://www.ceda.ac.uk). The archived verison will not include the ``_prelim`` postfix, and having gone through QC, may differ from the preliminary file.
Users can access the data by first registering as a CEDA user, and then applying for access to FAAM core data. The core data file is generally freely available, however access may be restricted for upto one year at the request of a project PI.

Other FAAM data products may require the core DECADES file to be available for
processing, or may require more work to process. These will be published in the 
CEDA archive as soon as they are available.


Usage License
-------------

FAAM data are licensed under the Open Government Licence (http://www.nationalarchives.gov.uk/doc/open-government-licence).
