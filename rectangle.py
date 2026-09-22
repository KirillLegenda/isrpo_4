import unittest

def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return a + b 


class RectangularTestClass(unittest.TestCase):
    def test_perimeter_1(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

        
    def test_perimeter_zero(self):
        res = perimeter(7, 0)
        self.assertEqual(res, 14)


    def test_perimeter_2(self):
        res = perimeter(5, 2)
        self.assertEqual(res, 14)


    def test_area_1(self):
        res = area(10, 5)
        self.assertEqual(res, 50)


    def test_area_2(self):
        res = area(5, 2)
        self.assertEqual(res, 10)

    def test_area_zero(self):
        res = area(6, 0)
        self.assertEqual(res, 0)

        