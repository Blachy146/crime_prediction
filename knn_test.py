import unittest
import unittest.mock
import Knn


class KnnTestSuite(unittest.TestCase):
    @unittest.mock.patch('distance_calculator.EuclideanDistance')
    @unittest.mock.patch('weight_calculators.ReverseFunctionCalculator')
    @unittest.mock.patch('weight_calculators.GaussCalculator')
    def setUp(self, DistanceMock, ReverseMock, GaussMock):
        attributes = [
            [1.0, 0.0],
            ["Bob", 1.0],
            [2.4, 0.0]]
        weights = [1, 2]

        self.distance_mock = DistanceMock()
        self.reverse_mock = ReverseMock()
        self.gauss_mock = GaussMock()

        self.distance_mock.calculate = unittest.mock.MagicMock()
        self.distance_mock.calculate.return_value = 1

        self.reverse_mock.calculate = unittest.mock.MagicMock()
        self.reverse_mock.calculate.return_value = 1

        self.gauss_mock.calculate = unittest.mock.MagicMock()
        self.gauss_mock.calculate.return_value = 1

        self.knn_reverse = Knn.Knn(attributes, self.distance_mock, self.reverse_mock, weights)
        self.knn_gauss = Knn.Knn(attributes, self.distance_mock, self.gauss_mock, weights)

    def test_prediction(self):
        self.assertEqual(self.knn_reverse.predict([1.0, 2.0], 2), 1.0)
        self.assertEqual(self.knn_gauss.predict([1.0, 2.0], 2), 1.0)


if __name__ == '__main__':
    unittest.main()
