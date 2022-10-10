from app.masks.rectangle import Rectangle
from app.point import Point
from app.mask_operations.union import mask_union


def test_nominal():
    rectangle1 = Rectangle(bottom_left_corner=Point(
        3, 4), top_right_corner=Point(6, 5))
    rectangle2 = Rectangle(bottom_left_corner=Point(
        0, 0), top_right_corner=Point(3, 3))

    union = mask_union(rectangle1, rectangle2)

    points_not_in_union = [Point(2, 5), Point(3, 7), Point(1, 8)]
    points_in_union = [Point(1, 2), Point(2, 1), Point(4.5, 4.5)]

    for point in points_in_union:
        assert union.point_is_hidden(point)

    for point in points_not_in_union:
        assert not union.point_is_hidden(point)
