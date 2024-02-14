from typing import Callable

filecodec: dict[str, dict[str, str|Callable|None]] = {
    'date': {
        'regex': '[0-9]{8}',
        'factory': lambda x: x.strftime('%Y%m%d')
    },
    'revision': {
        'regex': '[0-9]{3}',
        'factory': lambda x: f'{x:1d}'
    },
    'flight_number': {
        'regex': '[0-9]{3}',
        'factory': lambda x: x.lower()
    },
}