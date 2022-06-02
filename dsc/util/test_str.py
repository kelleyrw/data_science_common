import unittest

from dsc.util.str import (
    bool_or_none,
    empty_to_none,
    int_or_none,
    is_empty,
    is_not_empty,
    list_to_sql_str,
    strip_newline,
    to_int,
    zeros_to_none,
)


class TestStr(unittest.TestCase):
    def test_is_empty(self):
        self.assertFalse(is_empty("foo"))
        self.assertTrue(is_empty(""))

    def test_is_not_empty(self):
        self.assertTrue(is_not_empty("foo"))
        self.assertFalse(is_not_empty(""))

    def test_strip_newline(self):
        self.assertEqual(strip_newline("foo\n"), "foo")
        self.assertEqual(strip_newline("foo"), "foo")

    def test_empty_to_none(self):
        self.assertEqual(empty_to_none("foo"), "foo")
        self.assertIsNone(empty_to_none(""))

    def test_int_or_none(self):
        self.assertEqual(int_or_none("123"), int(123))
        self.assertIsNone(int_or_none("foo"))
        self.assertIsNone(int_or_none("foo123"))

    def test_bool_or_none(self):
        self.assertTrue(bool_or_none("foo", true_value="foo", false_value="bar"))
        self.assertFalse(bool_or_none("bar", true_value="foo", false_value="bar"))
        self.assertIsNone(bool_or_none("foobar", true_value="foo", false_value="bar"))

    def test_zeros_to_none(self):
        self.assertEqual(zeros_to_none("123"), int(123))
        self.assertIsNone(zeros_to_none("0"))
        self.assertIsNone(zeros_to_none("foo"))

    def test_to_int(self):
        self.assertEqual(to_int("foo"), int(-9999))
        self.assertEqual(to_int("foo", default=123), int(123))
        self.assertEqual(to_int("123"), int(123))

    def test_list_to_sql_str(self):
        self.assertEqual(list_to_sql_str([1, 2]), "(1, 2)")
        self.assertEqual(list_to_sql_str(["foo", "bar"]), "('foo', 'bar')")


if __name__ == "__main__":
    unittest.main()
