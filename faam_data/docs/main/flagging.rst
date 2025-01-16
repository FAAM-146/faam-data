----------------
Quality Flagging
----------------

Variables may have associated data quality variables, known as flags. These 
variables should be named ``<variable_name>_<quality-postfix>`` where ``<quality-postfix>``
is consistent within a data product. The data quality variable should also be referenced by name in the ``ancillary_variables`` attribute of the data variable.

For example, if a variable is named ``temperature`` and the quality postfix is ``flag``, then
the associated data quality variable should be named ``temperature_flag``:

.. code::

    temperature: {
        ...
        ancillary_variables: "temperature_flag"
        ...
    }

    temperature_flag: {
        ...
        coverage_content_type: "qualityInformation",
        flag_values: [0, 1, 2],
        flag_meanings: "data_good minor_data_quality_issue major_data_quality_issue"
    }

Flagging may be automatic, manual, or a combination of the two. Where the flagging
is manual, further information about the reason for flagging may be added to the ``comment`` attribute of the data quality variable.

Data which have a non-zero flag should be treated with caution, and the data
provider should be contacted if in doubt about whether data should be used.

Value-based Flags
-----------------

Value-based flags represent the quality of the corresponding data variable, with a flag value of 0 representing data which are presumed to be of sufficient quality. 
Larger values of the flag generally correspond to lower quality data, though this isn't always the case.

For example, consider a variable array with values

``1 2 6 5 4 3 6 5 4 3 2 1 4 5 6 7 7 6 5 3 2``

and its corresponding flag with values

``0 0 0 0 1 1 0 1 1 1 2 2 1 0 0 0 0 0 0 0 0``

To understand the meaning of these flag values, we can look at the ``flag_values`` and ``flag_meanings`` attributes of the flag variable, which may look like

* ``flag_meanings``: ``data_good minor_data_quality_issue major_data_quality_issue``
* ``flag_values``: ``0b 1b 2b``

We can see that there are three different flag meanings and three different flag values, and can deduce that a flag value of 0 indicates the data are considered good, a flag value of 1 indicates a minor data quality issue, and a flag value of 2 indicates a major data quality issue.
A user may choose, for example, to eliminate data with a major quality issue. To do this, they would simply mask/nan the variable wherever the flag variable has a value of 2, leaving the variable array as

``1 2 6 5 4 3 6 5 4 3 - - 4 5 6 7 7 6 5 3 2``.

Value-based flags will have the same dimensions as their associated variable, and the following variable attributes:

* ``_FillValue``: -128b
* ``standard_name``: 'status_flag' if the associated variable has no standard name, otherwise '<variable_standard_name> status_flag'
* ``long_name``: Flag for <variable_name>
* ``flag_values``: An array of the values that the flag variable can take. Typically runs from 0 to <length of flag_meanings> - 1.
* ``flag_meanings``: A space separated string of the meanings of each of the values in flag_values.

Bitmask flags
-------------

While the value-based flags map the values of an array to a single meaning, bitmask flags allow the representation of a boolean array for every ``flag_meaning``.
This is done by mapping each flag meaning to an increasing power of 2, which allows the representation of every possible state of every meaning using values from 1 to :math:`2^{\text{num. flags}-1}`.
A value of 0 indicates that no flags are set, and is set as a fill value.
In order to a bitmask flag it must first be unpacked. This adds to the complexity of using the flag, but makes flags much more powerful, so most variables in the FAAM core data product use bitmask flags.

For example, consider a variable array with values

``3 2 1 2 6 5 4 3 6 5 4 3 2 1 4 5 6 7 7 6 5 3 2``

and its corresponding flag with values

``0 0 1 1 3 3 2 2 4 4 4 4 6 6 6 6 8 8 5 5 3 3 1``

To understand the meaning of these flag values, we can look at the ``flag_masks`` and ``flag_meanings`` attributes of the flag variable, which may look like

* ``flag_meanings``: ``aircraft_on_ground flow_out_of_range temp_out_of_range data_out_of_bounds``
* ``flag_masks``: ``1b 2b 4b 8b``

There are four meanings, with each associated with a value of :math:`2^n` with :math:`n` taking the four values 0, 1, 2, 3. In the FAAM core data, flag values are guaranteed to be increasing powers of 2, thus the flag array can be unpacked simply by progressively right-bitshifting the flag array, and taking the result modulo 2.
In python, this can be achieved with the following code:

.. code::

    # Note that we don't need to worry about using the flag_masks attribute, as it
    # is guaranteed to be powers of 2 from 1 to 2^(n-1)
    unpacked = {}
    for i, meaning in enumerate(flag_var.flag_meanings.split()):
        unpacked[meaning] = (flag_data >> i) % 2

this would leave us with the following in ``unpacked``:

.. code::

    {
        aircraft_on_ground: array([0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]),
        flow_out_of_range: array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0]),
        temp_out_of_range: array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0]),
        data_out_of_bounds: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0])
    }

Bitmask flags will have the same dimensions as their associated variable, and the following variable attributes:

* ``_FillValue``: 0b
* ``standard_name``: 'status_flag' if the associated variable has no standard name, otherwise '<variable_standard_name> status_flag'
* ``long_name``: A descriptive name, indicating 
* ``valid_range``: The valid range of values in the flag variable array. Should be 1b, 2^(<number of flag_meanings>) - 1
* ``flag_masks``: An array of the values that the flag variable can take, which will runs from 1 to 2^(<number of flag_meanings> - 1).
* ``flag_meanings``: A space separated string of the meanings of each of the values in flag_values.

