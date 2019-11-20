import unittest
from src.driver.ScientificCalc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
    def test_case1(self):
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_sin('30'), -0.9880316240928618)

    def test_case2(self):
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_sin('uyh'), 'It is not number')

    def test_case3(self):
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_sin('-30'), 0.9880316240928618)
