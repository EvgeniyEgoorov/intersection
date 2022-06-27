import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rect1 = Rectangle(2, 2, 5, 6)
        self.rect2 = Rectangle(4, 4, 9, 9)
        self.rect3 = Rectangle(2, 2, 5, 7)
        self.rect4 = Rectangle(8, 8, 22, 44)


