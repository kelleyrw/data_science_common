# Standard library imports
import datetime as dt
from dataclasses import dataclass

# Third party imports
import pytest

# DSC imports
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
from dsc.util.obj import classproperty


@pytest.fixture()
def pset():
    @dataclass
    class PSet:
        d_fmt: str = "%Y-%m-%d"
        d_real_str: str = "1977-04-17"
        d_bogus_str: str = "19xx-04-17"

        t_fmt: str = "%Y-%m-%d %H:%M:%S"
        t_real_str: str = "1977-04-17 00:00:00"
        t_bogus_str: str = "19xx-04-17 00:00:00"

        @classproperty
        def d_real(cls) -> dt.date:
            return dt.datetime.strptime(cls.d_real_str, cls.d_fmt).date()

        @classproperty
        def t_real(cls) -> dt.date:
            return dt.datetime.strptime(cls.d_real_str, cls.d_fmt).date()

    return PSet()


def test_is_valid_datetime(pset):
    assert is_valid_datetime(pset.t_real_str)
    assert not is_valid_datetime(pset.t_bogus_str)
    fmt = "%Y-%m-%d 00:00:00"
    assert is_valid_datetime(pset.t_real_str, fmt)
    assert not is_valid_datetime(pset.t_bogus_str, fmt)


def test_is_valid_date(pset):
    assert is_valid_date(pset.d_real_str)
    assert not is_valid_date(pset.d_bogus_str)
    fmt = "%Y-%m-%d"
    assert is_valid_date(pset.d_real_str, fmt)
    assert not is_valid_date(pset.d_bogus_str, fmt)


def test_date_to_datetime(pset):
    t = date_to_datetime(pset.d_real)
    isinstance(t, dt.datetime)


def test_datetime_to_str(pset):
    s = datetime_to_str(pset.t_real)
    isinstance(s, str)


def test_str_to_datetime(pset):
    t = str_to_datetime(pset.t_real_str)
    isinstance(t, dt.datetime)


def test_date_to_str(pset):
    s = date_to_str(pset.d_real)
    isinstance(s, str)


def test_str_to_date(pset):
    d = str_to_date(pset.d_real_str)
    isinstance(d, dt.date)


def test_to_date(pset):
    d1 = to_date(pset.d_real_str)
    isinstance(d1, dt.date)
    d2 = to_date(pset.d_real)
    isinstance(d2, dt.date)
    d3 = to_date(pset.t_real)
    isinstance(d3, dt.date)
    d4 = to_datetime(pset.t_real_str)
    isinstance(d4, dt.date)


def test_to_str(pset):
    s1 = to_str(pset.d_real_str)
    isinstance(s1, str)
    s2 = to_str(pset.d_real)
    isinstance(s2, str)
    s3 = to_str(pset.t_real)
    isinstance(s3, str)
    s4 = to_str(pset.t_real_str, pset.t_fmt)
    isinstance(s4, str)


def test_to_datetime(pset):
    t1 = to_datetime(pset.d_real_str)
    isinstance(t1, dt.datetime)
    t2 = to_datetime(pset.d_real)
    isinstance(t2, dt.datetime)
    t3 = to_datetime(pset.t_real)
    isinstance(t3, dt.datetime)
    t4 = to_datetime(pset.t_real_str)
    isinstance(t4, dt.datetime)


def test_date_range(pset):
    d1 = to_date("1977-04-17")
    d2 = to_date("1977-04-20")
    dr = date_range(d1, d2)
    assert len(dr) == 4
