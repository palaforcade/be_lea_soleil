from app.masks.broken_line import BrokenLine
from app.point import Point


def test_nominal():
    broken_line = BrokenLine(Point(0, 3), Point(3, 4))
    hidden_point = Point(2, 1)
    not_hidden_point = Point(1, 4)

    assert broken_line.point_is_hidden(hidden_point)
    assert not broken_line.point_is_hidden(not_hidden_point)
