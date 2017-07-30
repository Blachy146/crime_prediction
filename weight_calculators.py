import math


class ReverseFunctionCalculator:
    def calculate(self, weight):
        if weight == 0:
            return 1.0
        else:
            return 1.0 / weight


class GaussCalculator:
    def __init__(self, sigma=10):
        self.sigma = sigma

    def calculate(self, weight):
        return math.exp(weight ** 2 / (2 * self.sigma ** 2))
