import datetime as dt
import unittest

from dsc.util.date import (
    date_range,
    date_to_datetime,
    date_to_str,
    datetime_to_str,
    is_valid_date,
    is_valid_datetime,
    str_to_date,
    str_to_datetime,
    to_date,
    to_datetime,
    to_str,
)


class TestDate(unittest.TestCase):
    def setUp(self) -> None:

        self.d_fmt = "%Y-%m-%d"
        self.d_real_str = "1977-04-17"
        self.d_bogus_str = "19xx-04-17"
        self.d_real = dt.datetime.strptime(self.d_real_str, self.d_fmt).date()

        self.t_fmt = "%Y-%m-%d %H:%M:%S"
        self.t_real_str = "1977-04-17 00:00:00"
        self.t_bogus_str = "19xx-04-17 00:00:00"
        self.t_real = dt.datetime.strptime(self.t_real_str, self.t_fmt)

    def test_is_valid_datetime(self):
        self.assertTrue(is_valid_datetime(self.t_real_str))
        self.assertFalse(is_valid_datetime(self.t_bogus_str))
        fmt = "%Y-%m-%d 00:00:00"
        self.assertTrue(is_valid_datetime(self.t_real_str, fmt))
        self.assertFalse(is_valid_datetime(self.t_bogus_str, fmt))

    def test_is_valid_date(self):
        self.assertTrue(is_valid_date(self.d_real_str))
        self.assertFalse(is_valid_date(self.d_bogus_str))
        fmt = "%Y-%m-%d"
        self.assertTrue(is_valid_date(self.d_real_str, fmt))
        self.assertFalse(is_valid_date(self.d_bogus_str, fmt))

    def test_date_to_datetime(self):
        t = date_to_datetime(self.d_real)
        self.assertIsInstance(t, dt.datetime)

    def test_datetime_to_str(self):
        s = datetime_to_str(self.t_real)
        self.assertIsInstance(s, str)

    def test_str_to_datetime(self):
        t = str_to_datetime(self.t_real_str)
        self.assertIsInstance(t, dt.datetime)

    def test_date_to_str(self):
        s = date_to_str(self.d_real)
        self.assertIsInstance(s, str)

    def test_str_to_date(self):
        d = str_to_date(self.d_real_str)
        self.assertIsInstance(d, dt.date)

    def test_to_date(self):
        d1 = to_date(self.d_real_str)
        self.assertIsInstance(d1, dt.date)
        d2 = to_date(self.d_real)
        self.assertIsInstance(d2, dt.date)
        d3 = to_date(self.t_real)
        self.assertIsInstance(d3, dt.date)
        d4 = to_datetime(self.t_real_str)
        self.assertIsInstance(d4, dt.date)

    def test_to_str(self):
        s1 = to_str(self.d_real_str)
        self.assertIsInstance(s1, str)
        s2 = to_str(self.d_real)
        self.assertIsInstance(s2, str)
        s3 = to_str(self.t_real)
        self.assertIsInstance(s3, str)
        s4 = to_str(self.t_real_str, self.t_fmt)
        self.assertIsInstance(s4, str)

    def test_to_datetime(self):
        t1 = to_datetime(self.d_real_str)
        self.assertIsInstance(t1, dt.datetime)
        t2 = to_datetime(self.d_real)
        self.assertIsInstance(t2, dt.datetime)
        t3 = to_datetime(self.t_real)
        self.assertIsInstance(t3, dt.datetime)
        t4 = to_datetime(self.t_real_str)
        self.assertIsInstance(t4, dt.datetime)

    def test_date_range(self):
        d1 = to_date("1977-04-17")
        d2 = to_date("1977-04-20")
        dr = date_range(d1, d2)
        self.assertEqual(len(dr), 4)


if __name__ == "__main__":
    unittest.main()
