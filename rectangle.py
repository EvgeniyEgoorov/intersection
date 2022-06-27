from dataclasses import dataclass


@dataclass
class Rectangle:
    """For each rectangle, we set the lower left and upper right vertices (x, y)"""
    x_min: int
    y_min: int
    x_max: int
    y_max: int


