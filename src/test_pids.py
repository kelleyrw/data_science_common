import pids


def test_from_int():
    assert pids.pid.from_int(15) == "F"


def test_to_int():
    assert pids.pid.to_int("F") == 15
