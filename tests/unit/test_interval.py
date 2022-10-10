from app.interval import Interval


def test_nominal_interval():
    interval = Interval(2, 8)
    value = 4
    assert interval.contains(value)


def test_null_interval():
    interval = Interval(4, 4)
    assert not interval.contains(8)
