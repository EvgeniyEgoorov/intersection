import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rect1 = Rectangle(2, 2, 5, 6)
        self.rect2 = Rectangle(4, 4, 9, 9)
        self.rect3 = Rectangle(2, 2, 5, 7)
        self.rect4 = Rectangle(8, 8, 22, 44)

    def test_has_intersection(self):
        """
        First scenario returns AssertionError if rectangles have no intersection (!= True)
        Second scenario returns AssertionError if rectangles have intersection (!= False)
        """
        self.assertTrue(Rectangle.has_intersection(self.rect1, self.rect2), "No intersection")
        self.assertFalse(Rectangle.has_intersection(self.rect3, self.rect4), "There is an intersection")


if __name__ == '__main__':
    unittest.main()
