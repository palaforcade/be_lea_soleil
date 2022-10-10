from app.masks.mask import Mask
from app.point import Point
from app.interval import Interval


class Rectangle(Mask):
    def __init__(self, *, top_right_corner: Point, bottom_left_corner: Point):
        self.elevation_interval = Interval(
            top_right_corner.elevation, bottom_left_corner.elevation)
        self.azimut_interval = Interval(top_right_corner.azimut,
                                        bottom_left_corner.azimut)

    def point_is_hidden(self, point: Point) -> bool:
        return (
            self.elevation_interval.contains(
                point.elevation) and self.azimut_interval.contains(point.azimut)
        )
