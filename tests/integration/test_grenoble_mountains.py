from app.masks.broken_line import BrokenLine
from app.point import Point

test_broken_line = BrokenLine(Point(-180, 13.8), Point(-170, 18.9), Point(-145, 1.98), Point(-120, 18.3), Point(-96.1, 17.3), Point(-60.8, 6.2), Point(-14, 2.8), Point(-8.4, 5.6), Point(
    0.8, 2.6), Point(21.6, 5.5), Point(38.1, 14.6), Point(49.4, 8.9), Point(60.1, 11.3), Point(87.4, 10.4), Point(99.3, 12), Point(142.1, 2.6), Point(157.8, 4), Point(175.1, 17.1), Point(180, 15.9))


def test_point():
    assert test_broken_line.point_is_hidden(Point(-112.2, 10.93))
