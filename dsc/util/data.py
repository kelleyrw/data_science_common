from typing import Any, Iterable

import numpy

# fmt: off
__all__ = [
    "list_contains_type",
]
# fmt: on


def list_contains_type(
    value: Iterable[Any], test_type: type, require_non_empty: bool = False
) -> bool:
    """
    Determine if a list contains the given type.

    Args:
        value (): list or numpy array to test
        test_type (): python type to test
        require_non_empty ():
            True: empty list returns False
            False: empty list returns True (default)

    Returns:
        boolean
    """

    if isinstance(value, numpy.ndarray):
        value = value.tolist()

    result = isinstance(value, Iterable) and all(
        isinstance(i, test_type) for i in value
    )
    if require_non_empty:
        result = result and len(value) > 0
    return result
