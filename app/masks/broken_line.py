from typing import Tuple
from app.masks.mask import Mask
from app.point import Point
from app.interval import Interval


class BrokenLine(Mask):
    def __init__(self, *points: Tuple[Point]) -> None:
        self.points = sorted(points, key=lambda point: point.azimut)

    def image_by_affine_function(left_point: Point, right_point: Point, azimut: float):
        assert Interval(left_point.azimut, right_point.azimut).contains(
            azimut), "The provided azimut isn't in the definition interval of the affine function provided"
        director_coefficient = (
            right_point.elevation - left_point.elevation)/(right_point.azimut - left_point.azimut)
        return left_point.elevation + director_coefficient*(azimut - left_point.azimut)

    def point_is_hidden(self, point: Point):
        for i in range(len(self.points) - 1):
            interval = Interval(
                self.points[i].azimut, self.points[i + 1].azimut)
            if interval.contains(point.azimut):
                broken_line_elevation = BrokenLine.image_by_affine_function(
                    self.points[i], self.points[i+1], point.azimut)
                return point.elevation <= broken_line_elevation
        raise "The provided point is out of range for the current BrokenLine instance"
