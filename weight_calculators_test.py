import unittest
import weight_calculators as calculators


class ReverseFunctionCalculatorTestSuite(unittest.TestCase):
    def setUp(self):
        self.calculator = calculators.ReverseFunctionCalculator()

    def test_should_return_correct_weight(self):
        weight1 = 1.0
        weight2 = 0.6
        weight3 = 2.4
        correct_result1 = 1.0
        correct_result2 = 1.666
        correct_result3 = 0.416

        self.assertAlmostEqual(self.calculator.calculate(weight1), correct_result1, delta=0.001)
        self.assertAlmostEqual(self.calculator.calculate(weight2), correct_result2, delta=0.001)
        self.assertAlmostEqual(self.calculator.calculate(weight3), correct_result3, delta=0.001)


class GaussCalculatorTestSuite(unittest.TestCase):
    def setUp(self):
        self.calculator = calculators.GaussCalculator()

    def test_should_return_correct_weight(self):
        weight1 = 1.0
        weight2 = 0.6
        weight3 = 2.4
        correct_result1 = 1.005
        correct_result2 = 1.001
        correct_result3 = 1.029

        self.assertAlmostEqual(self.calculator.calculate(weight1), correct_result1, delta=0.001)
        self.assertAlmostEqual(self.calculator.calculate(weight2), correct_result2, delta=0.001)
        self.assertAlmostEqual(self.calculator.calculate(weight3), correct_result3, delta=0.001)


if __name__ == '__main__':
    unittest.main()
