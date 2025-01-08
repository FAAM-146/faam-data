=====================================
Adding a data product to the standard
=====================================

A data product can be added to the standard by supplying a `yaml` formatted
file describing the product in a format understood by the `vocal` tool, implementing
all required metadata in this standard. The definition should take the following format:

.. code-block:: yaml

    meta: 
        file_pattern: "some_pattern_{date}_{flight_number}.nc"
        long_name: "Some data product"
        short_name: "some_data_product"
        description: "A longer description of the data product"
        references: 
            - title: "Some reference"
              web: "http://some.url"
              doi: "10.1234/5678"
    attributes:
        Conventions: "CF-1.6 ACDD-1.3"
        acknowledgements: "Some acknowledgement"
        # ... other attributes
    dimensions:
        - name: time
          size: null # null (or blank) means unlimited
        - name: height
          size: 100
    variables:
        - meta:
            name: "some_variable"
            datatype: "<datatype>" # e.g. float32, int32, str, etc.
          dimensions: # Subset of dimensions defined above
            - time
            - height
          attributes:
            long_name: "Some variable"
            units: "m/s"
            # ... other attributes
        # ... other variables
    groups: # optional
        # nested groups, following the same structure as the root group above

Attributes can be specified as literals, or it may be indicated that they are
going to be generated on-the-fly during data processing. In this case, the
attribute should be specified using a `derived_from_file` indicator. For example:

.. code-block:: yaml

    attributes:
        comment: "<str: derived_from_file>"  # A string defined at runtime
        revision: "<int8: derived_from_file>"  # An integer defined at runtime
        revision_comment: "<str: derived_from_file optional>"  # An optional string defined at runtime"
        actual_range: "<Array[float32]: derived_from_file>"  # An array of floats defined at runtime