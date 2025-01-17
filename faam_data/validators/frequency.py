from typing import Annotated
from vocal.validation import vocal_validator, Model


@vocal_validator(
    description=(
        "Ensures that frequency attribute is present when using sps dimension"
        "and that it matches the sps dimension"
    ),
    bound=Model.after
)
def validate_frequency(cls, v):
    """
    Ensures that the frequency attribute is present when using sps dimension
    and that it matches the sps dimension.

    This validator should be applied as a model validator to the
    'Variable' model.

    Args:
        v (Variable): The variable to validate

    Returns:
        Variable: The variable if it is valid

    Raises:
        ValueError: If the frequency attribute is missing or does not match the sps dimension
    """
    frequency = v.attributes.frequency
    has_sps_dim = any([d.startswith("sps") for d in v.dimensions])
    if frequency is None and has_sps_dim:
        raise ValueError('"frequency" attribute is required when using sps dimension')

    if not has_sps_dim:
        return v

    sps_dim = [d for d in v.dimensions if d.startswith("sps")][0]
    sps_dim_int = int(sps_dim.replace("sps", ""))

    if frequency != sps_dim_int:
        raise ValueError(
            f'"frequency" attribute must match the sps dimension. '
            f"Expected {sps_dim_int}, got {frequency}"
        )

    return v
