from typing import Optional

# fmt: off
__all__ = [
    "empty",
    "strip_newline",
    "empty_to_none",
    "not_empty",
    "int_or_none",
    "bool_or_none",
    "zeros_to_none",
    "list_to_sql_str"
]
# fmt: on


def empty(value: str) -> bool:
    """
    determine if a string is empty

    Args:
        value (): string to check

    Returns:
        boolean
    """
    return value is None or value == ""


def not_empty(value: str) -> bool:
    """
    determine if a string is NOT empty

    Args:
        value (): string to check

    Returns:
        boolean
    """
    return not empty(value)


def strip_newline(line: str) -> str:
    """
    strips the newline characters from the end of a string

    Args:
        line (): string to check

    Returns:
        str
    """
    return line.rstrip("\n\r").rstrip("\n")


def empty_to_none(value: str) -> Optional[str]:
    """
    returns value if the string is not empty, else returns None

    Args:
        value (): string to check

    Returns:
        Optional[str]
    """
    assert isinstance(value, str), "must be a str type"
    value = value.strip()
    return value if not_empty(value) else None


def int_or_none(value: str) -> Optional[int]:
    """
    returns int if value contains digits, else returns None

    Args:
        value (): string to check

    Returns:
        Optional[int]
    """
    assert isinstance(value, str), "must be a str type"
    return int(value) if value.isdigit() else None


def bool_or_none(value: str, true_value: str, false_value: str) -> Optional[bool]:
    """
    returns bool based on true_value and false_value; else returns None

    Args:
        value (): string to check
        true_value (): string to compare for True
        false_value (): string to compare for False

    Returns:
        Optional[bool]
    """
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

    Args:
        value (): string to extract zeros

    Returns:
        Optional[int]
    """
    if value.isdigit():
        result = int(value)
        result = None if result == 0 else result
        return result
    else:
        return None


def list_to_sql_str(values: list) -> str:
    """
    covert a list to a sql compliant list.
    e.g. [1, 3, 4] -> "(1, 2, 3)"
    e.g. ['foo', 'bar'] -> "('foo', 'bar')"

    Args:
        values (): list to convert

    Returns:
        str
    """

    if all(isinstance(i, str) for i in values):
        str_type = type(values[0]) if len(values) > 0 else str
        items_str = ["'%s'" % str_type(s).replace("'", "''") for s in values]
    else:
        items_str = [str(s) for s in values]
    result = "(%s)" % ", ".join(items_str)
    return result
