"""
================================================================================
module: lrc.util.str
================================================================================

A collection of helper functions for string manipulation

.. code-block:: python

  from lrc.util.str import <module_name>
"""
from typing import Optional


def is_empty(value: str) -> bool:
    """
    determine if a string is empty

    Args:
        value ():

    Returns:

    """
    """
    determine if a string is empty

    :param value: string to check
    :type value: str
    :return: boolean val
    :rtype: bool
    """
    return value == ""


def is_not_empty(value: str) -> bool:
    """
    determine if a string is not empty

    :param value: string to check
    :type value: str
    :return: boolean val
    :rtype: bool
    """
    return value != ""


def strip_newline(line: str) -> str:
    """
    strips the newline characters from the end of a string

    :param line: string to check
    :type line: str
    :return: string
    :rtype: str
    """
    return line.rstrip("\n\r").rstrip("\n")


def empty_to_none(value: str) -> Optional[str]:
    """
    returns value if the string is not empty, else returns None

    :param value: string to check
    :type value: str
    :return: string or None
    :rtype: Optional[str]
    """
    assert isinstance(value, str), "must be a str type"
    value = value.strip()
    return value if is_not_empty(value) else None


def int_or_none(value: str) -> Optional[int]:
    """
    returns int if value contains digits, else returns None

    :param value: int to check
    :type value: str
    :return: int or None
    :rtype: Optional[int]
    """
    assert isinstance(value, str), "must be a str type"
    return int(value) if value.isdigit() else None


def bool_or_none(value: str, true_value: str, false_value: str) -> Optional[bool]:
    """
    returns bool based on true_value and false_value; else returns None

    :param value: string to check
    :type value: str
    :param true_value: string to compare for True
    :type true_value: str
    :param false_value: string to compare for False
    :type false_value: str
    :return: bool or None
    :rtype: Optional[bool]
    """
    assert isinstance(value, str), "must be a str type"
    value = empty_to_none(value)
    if value is None:
        return None
    elif value == true_value:
        return True
    elif value == false_value:
        return False
    else:
        return None


def zeros_to_none(value: str) -> Optional[int]:
    """
    returns int if non-zero, else returns None

    :param value: string to extract int
    :type value: str
    :return: int or None
    :rtype: Optional[int]
    """
    assert isinstance(value, str), "value must be a str type"
    if value.isdigit():
        result = int(value)
        result = None if result == 0 else result
        return result
    else:
        return None


def to_int(value: str, default: int = -9999) -> int:
    """
    covert a string to an int; returns default if str is not numeric

    :param value: string to convert to int
    :type value: str
    :param default: default to return if value is not numeric
    :type default: int
    :return: int from value
    :rtype: int
    """
    assert isinstance(value, str), "value must be a str type"
    return int(value) if value.isdigit() else default


def list_to_sql_str(items: list):
    """
    covert a list to a sql complient list.
    e.g. [1, 3, 4] -> '(1, 2, 3)'

    :param items: list to convert
    :type value: str
    :return: str
    :rtype: str
    """
    if all(isinstance(i, str) for i in items):
        str_type = type(items[0]) if len(items) > 0 else str
        items_str = ["'%s'" % str_type(s).replace("'", "''") for s in items]
    else:
        items_str = [str(s) for s in items]
    result = "(%s)" % ", ".join(items_str)
    return result
