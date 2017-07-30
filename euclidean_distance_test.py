import unittest
import distance_calculator as calculator


class EuclideanDistanceTestSuite(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.EuclideanDistance()

    def test_should_return_correct_distance(self):
        instance1 = [6, 5]
        instance2 = [1, 1]
        weights = [3, 2]
        correct_result = 10.344

        self.assertAlmostEqual(self.calculator.calculate(instance1, instance2, weights), correct_result, delta=0.001)


if __name__ == '__main__':
    unittest.main()
