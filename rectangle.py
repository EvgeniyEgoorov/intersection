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

    @classmethod
    def handler(cls, arr: list) -> list:
        """The function handles an array of rectangles coordinates"""
        ls = [0 for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if cls.has_intersection(arr[i], arr[j]):
                    ls[i] += 1
                    ls[j] += 1
        return ls


if __name__ == '__main__':
    n = int(input())
    rectangles = [Rectangle(*list(map(int, input().split()))) for _ in range(n)]
    print(*Rectangle.handler(rectangles))
