import unittest

def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 


class TriangleTestClass(unittest.TestCase):
    def test_area_0(self):
        res = area(0, 8)
        self.assertEqual(res, 0)


    def test_area_1(self):
        res = area(4, 5)
        self.assertEqual(res, 10)


    def test_area_2(self):
        res = area(5, 12)
        self.assertEqual(res, 30)


    def test_perimeter_0(self):
        res = perimeter(0, 8, 9)
        self.assertEqual(res, 17)


    def test_perimeter_1(self):
        res = perimeter(4, 5, 6)
        self.assertEqual(res, 15)


    def test_perimeter_2(self):
        res = perimeter(5, 12, 13)
        self.assertEqual(res, 30)
