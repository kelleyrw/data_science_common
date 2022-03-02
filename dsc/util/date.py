"""

"""
import datetime as dt

__all__ = [
    "is_valid_datetime",
]


def is_valid_datetime(value: str, format: str = "%Y-%m-%d %H:%M:%S") -> bool:
    """
    Determine if string value represents valid datetime.

    Parameters
    ----------
    value : str
        string to test
    format :  str
        format to validate against

    Returns
    -------
    bool
    """
    try:
        dt.datetime.strptime(value, format)
        return True
    except ValueError:
        return False
