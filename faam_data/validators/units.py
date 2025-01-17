import cfunits  # type: ignore # no type hints available

from vocal.validation import vocal_validator, Attribute


@vocal_validator(
    description="Ensure that units attribute is a valid CFUnits string",
    bound=Attribute("units")
)
def validate_units(cls, units: str) -> str:
    """
    This validator should be applied as a field validator to the
    'units' attribute of the variable attributes model.

    It ensures that:
        - The units string is a valid UDUNITS string

    Args:
        units: The units string to validate

    Returns:
        str: The units string if it is valid

    Raises:
        ValueError: If the units string is not valid
    """
    parsed = cfunits.Units(units)
    if not parsed.isvalid:
        raise ValueError(f"Invalid units string: {units} ({parsed.reason_notvalid})")
    return units
