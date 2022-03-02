"""
================================================================================
module: dsc.util.date
================================================================================

A collection of unitlity functions for date and time manipulation

.. code-block:: python

  from dsc.util.date import <method_name>
"""
import datetime as dt

__all__ = [
    "is_valid_datetime",
]


def is_valid_datetime(value: str, format: str = "%Y-%m-%d %H:%M:%S") -> bool:
    """
    Determine if string value represents valid datetime.

    :param value: string to test
    :param format: format to validate against
    :return: bool
    """
    try:
        dt.datetime.strptime(value, format)
        return True
    except ValueError:
        return False
