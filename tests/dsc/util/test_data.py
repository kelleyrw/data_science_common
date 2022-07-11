# DSC imports
from dsc.util.data import list_contains_type


def test_list_contains_type():

    assert list_contains_type([1, 2, 3], int)
    assert list_contains_type(["foo", "bar"], str)
    assert not list_contains_type([1, 2, 3], str)
    assert not list_contains_type(["foo", "bar"], int)
    assert list_contains_type([], int)
    assert list_contains_type([], str)

    assert list_contains_type([1, 2, 3], int, require_non_empty=True)
    assert list_contains_type(["foo", "bar"], str, require_non_empty=True)
    assert not list_contains_type([], int, require_non_empty=True)
    assert not list_contains_type([], str, require_non_empty=True)
