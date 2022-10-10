from abc import ABC, abstractmethod
from typing import List
import matplotlib.pyplot as plt

from app.point import Point


class Mask(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def point_is_hidden(self, point: Point) -> bool:
        raise NotImplementedError
