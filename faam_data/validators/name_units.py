import cfunits  # type: ignore # no type hints available

from typing import Protocol

from vocal.validation import vocal_validator, Model
from vocal.vocab import CFStandardNames


standard_names = CFStandardNames()


class HasUnitsAndName(Protocol):
    units: str
    standard_name: str


@vocal_validator(
    description="Ensure that units are compatible with given standard name.",
    bound=Model.after,
)
def validate_units_compatible_with_name[T: HasUnitsAndName](cls, attributes: T) -> T:
    units = getattr(attributes, "units", None)
    standard_name = getattr(attributes, "standard_name", None)

    # If units or standard_name are not present, we can't validate
    if units is None or standard_name is None:
        return attributes
    
    # We can't validate time units as canonical units 's' are not considered
    # equivalent to 'seconds since 1970-01-01 00:00:00'
    if standard_name == "time":
        return attributes

    canonical_units = standard_names.canonical_units(standard_name)
    if canonical_units is None:
        return attributes

    parsed = cfunits.Units(units)
    canonical = cfunits.Units(canonical_units)

    if parsed.equivalent(canonical):
        return attributes

    raise ValueError(
        f"Units '{units}' are not compatible with standard name '{standard_name}'"
    )
