import datetime as dt
import unittest

from dsc.util.date import is_valid_datetime


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


if __name__ == "__main__":
    unittest.main()
