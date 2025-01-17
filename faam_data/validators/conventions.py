from vocal.validation import vocal_validator

@vocal_validator(description='Ensure that Conventions string includes ACDD-1.3, CF-1.9 or later, and a FAAM convention')
def validate_conventions(cls, conventions: str) -> str:
    """
    This validator should be applied as a field validator to the
    'Conventions' attribute of the global attributes model.

    It ensures that:
        - Conventions are space rather than comma separated
        - The dataset declares compliance with ACDD-1.3
        - The dataset declares compliance with CF-1.9 or later
        - The dataset declares compliance with a FAAM convention

    Args:
        conventions (str): The conventions string to validate

    Returns:
        str: The conventions string if it is valid
    """
    if ',' in conventions:
        raise ValueError('Conventions should be space separated')
    
    errors: list[str] = []

    conventions_list = conventions.split()

    # Must identify with ACDD-1.3
    if 'ACDD-1.3' not in conventions_list:
        errors.append('Dataset must comply with the Attribute Convention for Dataset Discovery 1.3 (ACDD-1.3)')
    
    # Must identify with CF-1.9 or later, but not CF-2.0 if that becomes a thing
    try:
        cf_str = [c for c in conventions_list if c.startswith('CF-')][0]
        cf_version = float(cf_str.split('-')[1])
        if cf_version < 1.9 or cf_version >= 2.0:
            errors.append('Dataset must comply with the CF conventions version >=1.9, <2.0')

    except IndexError:
        errors.append('Dataset must comply with a CF conventions (CF-x.y)')
        
    except ValueError:
        errors.append(f'CF version {cf_str} not understood')

    # Must identify with a FAAM convention
    if not any([c.startswith('FAAM-') for c in conventions_list]):
        errors.append('Dataset must comply with a FAAM convention (FAAM-x.y)')

    if errors:
        raise ValueError('. '.join(errors))

    return conventions