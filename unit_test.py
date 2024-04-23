import unittest

def calculate_area(length, width):
    if length <= 0 or width <=0:
        return None
    return length * width

class TestCalculation(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(calculate_area(5, 4), 20)
        self.assertEqual(calculate_area(7, 6), 42)

    def test_zero_value(self):
        self.assertEqual(calculate_area(5, 0), 5)
        self.assertEqual(calculate_area(0, 5), None)
        self.assertEqual(calculate_area(0, 0), None)    

    def test_negative_value(self):
        self.assertEqual(calculate_area(-5, 6), None)
        self.assertEqual(calculate_area(6, -9), None)
        self.assertEqual(calculate_area(-4,-9), 36)
    
    def test_large_value(self):
        self.assertEqual(calculate_area(6985, 1633), 11406505)

    def test_float_value(self):
        self.assertEqual(calculate_area(3.6, 1.9), 6.84)

if __name__ == '__main__': 
    unittest.main()       
