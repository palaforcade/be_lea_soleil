from math import sqrt


class Point:

    def __init__(self, azimut: float, elevation: float):
        self.azimut: float = azimut
        self.elevation: float = elevation

    def distance(self, other_point):
        dist = sqrt((self.elevation - other_point.elevation) **
                    2 + (self.azimut - other_point.azimut)**2)
        return dist

    def __str__(self) -> str:
        return f"Point({self.azimut}, {self.elevation})"
