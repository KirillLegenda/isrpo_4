import math
import unittest


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

class CircleTestClass(unittest.TestCase):
    def test_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)


    def test_area_1(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)


    def test_area_2(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)


    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


    def test_perimeter_1(self):
        res = perimeter(4)
        self.assertEqual(res, 25.132741228718345)


    def test_perimeter_2(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)