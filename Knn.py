import collections
import operator


class Knn:
    def __init__(self, data, distance_calculator, weight_calculator, weights):
        self.data = data
        self.distance_calculator = distance_calculator
        self.weight_calculator = weight_calculator
        self.weights = weights

    def predict(self, instance, neighbours):
        self._calculate_nearest_neighbours(instance)
        return 1.0

    def _calculate_nearest_neighbours(self, instance):
        distances = {}

        for other_instance in self.data:
            distance = self.distance_calculator.calculate(instance, other_instance)
            distances[len(distances)] = distance
        distances = collections.OrderedDict(sorted(distances.items(), key=operator.itemgetter(1)))

        return distances

