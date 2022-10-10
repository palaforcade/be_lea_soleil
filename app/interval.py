from doctest import FAIL_FAST


class Interval:
    def __init__(self, first_value, second_value) -> None:
        if first_value <= second_value:
            self.lower_value = first_value
            self.upper_value = second_value
        else:
            self.lower_value = second_value
            self.upper_value = first_value

    def contains(self, value: float):
        return (
            value <= self.upper_value and value >= self.lower_value
        )
