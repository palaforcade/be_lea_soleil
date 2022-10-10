from typing import Tuple


from app.masks.mask import Mask
from typing import Tuple
from app.point import Point


def mask_intersection(*masks: Tuple[Mask]):

    class UnionMask(Mask):
        def point_is_hidden(self, point: Point):
            for mask in masks:
                if not mask.point_is_hidden(point):
                    return False
            return True

    return UnionMask()
