# DSC imports
from dsc.util.str import (
    bool_or_none,
    empty,
    empty_to_none,
    int_or_none,
    list_to_sql_str,
    not_empty,
    strip_newline,
    zeros_to_none,
)


def test_is_empty():
    assert not empty("foo")
    assert empty("")
    assert empty(None)


def test_is_not_empty():
    assert not_empty("foo")
    assert not not_empty("")


def test_strip_newline():
    assert strip_newline("foo\n") == "foo"
    assert strip_newline("foo") == "foo"


def test_empty_to_none():
    assert empty_to_none("foo") == "foo"
    assert empty_to_none("") is None


def test_int_or_none():
    assert int_or_none("123") == int(123)
    assert int_or_none("foo") is None
    assert int_or_none("foo123") is None


def test_bool_or_none():
    assert bool_or_none("foo", true_value="foo", false_value="bar")
    assert not bool_or_none("bar", true_value="foo", false_value="bar")
    assert bool_or_none("foobar", true_value="foo", false_value="bar") is None


def test_zeros_to_none():
    assert zeros_to_none("123") == int(123)
    assert zeros_to_none("0") is None
    assert zeros_to_none("foo") is None


def test_list_to_sql_str():
    assert list_to_sql_str([]) == "()"
    assert list_to_sql_str([1, 2]) == "(1, 2)"
    assert list_to_sql_str(["foo", "bar"]) == "('foo', 'bar')"
