import unittest
from square import area, perimeter

class SquareTestClass(unittest.TestCase):
    def test_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)


    def test_area_1(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_2(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


    def test_perimeter_1(self):
        res = perimeter(4)
        self.assertEqual(res, 16)


    def test_perimeter_2(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    

if __name__ == '__main__':
    unittest.main()