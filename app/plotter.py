import matplotlib.pyplot as plt
import numpy as np

from app.masks.mask import Mask
from app.masks.rectangle import Rectangle
from app.interval import Interval
from app.point import Point
from app.masks.broken_line import BrokenLine


class Canvas:
    def __init__(self, *, azimut_interval: Interval, elevation_interval: Interval, delta_azimut, delta_elevation) -> None:
        azimut_range = np.arange(
            azimut_interval.lower_value, azimut_interval.upper_value, delta_azimut)
        elevation_range = np.arange(
            elevation_interval.lower_value, elevation_interval.upper_value, delta_elevation)

        self.visible_points_list = []
        for azimut in azimut_range:
            for elevation in elevation_range:
                self.visible_points_list.append(Point(azimut, elevation))

    def add_mask(self, mask: Mask):
        for point in self.visible_points_list:
            if mask.point_is_hidden(point):
                self.visible_points_list.remove(point)

    def plot(self):
        azimut_list, elevation_list = [], []
        for point in self.visible_points_list:
            azimut_list.append(point.azimut)
            elevation_list.append(point.elevation)

        scatter_area = 1
        plt.scatter(azimut_list, elevation_list, s=scatter_area)
        plt.show()


if __name__ == "__main__":
    test_broken_line = BrokenLine(Point(-180, 13.8), Point(-170, 18.9), Point(-145, 1.98), Point(-120, 18.3), Point(-96.1, 17.3), Point(-60.8, 6.2), Point(-14, 2.8), Point(-8.4, 5.6), Point(
        0.8, 2.6), Point(21.6, 5.5), Point(38.1, 14.6), Point(49.4, 8.9), Point(60.1, 11.3), Point(87.4, 10.4), Point(99.3, 12), Point(142.1, 2.6), Point(157.8, 4), Point(175.1, 17.1), Point(180, 15.9))
    canvas = Canvas(azimut_interval=Interval(-180, 180),
                    elevation_interval=Interval(0, 90), delta_azimut=1, delta_elevation=1)

    rectangle = Rectangle(top_right_corner=Point(
        20, 40), bottom_left_corner=Point(-20, 0))

    canvas.add_mask(rectangle)
    canvas.add_mask(test_broken_line)
    canvas.plot()
