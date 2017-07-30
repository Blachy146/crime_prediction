import math


class EuclideanDistance:
    def calculate(self, instance1, instance2, weights):
        result = 0.0
        for (a, b, weight) in zip(instance1, instance2, weights):
            result += ((a - b) ** 2) * weight

        return math.sqrt(result)
