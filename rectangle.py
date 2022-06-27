from dataclasses import dataclass


@dataclass
class Rectangle:
    """For each rectangle, we set the lower left and upper right vertices (x, y)"""
    x_min: int
    y_min: int
    x_max: int
    y_max: int

    @staticmethod
    def has_intersection(rect1, rect2):
        """The logic is based on Separating Axis Theorem"""
        return any([
            rect1.x_min < rect2.x_min < rect1.x_max,
            rect1.x_min < rect2.x_max < rect1.x_max,
            rect1.y_min < rect2.y_min < rect1.y_max,
            rect1.y_min < rect2.y_max < rect1.y_max,
        ])


if __name__ == '__main__':
    first_rect = Rectangle(1, 1, 5, 5)
    second_rect = Rectangle(4, 4, 9, 9)
    print(Rectangle.has_intersection(first_rect, second_rect))
