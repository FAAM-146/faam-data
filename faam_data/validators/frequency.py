from vocal.validation import vocal_validator

@vocal_validator(description='Ensure that frequency attribute is present when using sps dimension')
def validate_frequency(cls, v):
        frequency = v.attributes.frequency
        has_sps_dim = any([d.startswith("sps") for d in v.dimensions])
        if frequency is None and has_sps_dim:
            raise ValueError(
                '"frequency" attribute is required when using sps dimension'
            )
        return v