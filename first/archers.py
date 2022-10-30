from first.generators.prand import Generators
from scipy import stats
import matplotlib.pyplot as plt
from numpy import random as ran
import numpy as np
from collections import Counter
import math
import statistics
# TODO: dodaj test dla średnich 
# TODO: dodaj punktowanie za strzał
class Archers:
    def __init__(self,  shield_x=8000, shield_y=8000) -> None:
        self.max_error_distance = 1000
        self.max_error_x_distance = 900
        self.max_error_y_distance = 900
        self.first_points = []
        self.second_points = []
        self.shield_x = shield_x
        self.shield_y = shield_y
        self.shield_rad = math.sqrt(shield_x ** 2 + shield_y **2)

    def first(self, tries=10):
        self.first_points = []
        distance_generator = Generators.LCG(max=self.max_error_distance)
        for _ in range(tries):
            p =next(distance_generator)
            if p <= self.shield_rad:
                self.first_points.append(p)
        return None

    def second(self, tries=10):
        self.second_points = []
        x_genrator = Generators.LCG(max=self.max_error_x_distance)
        y_genrator = Generators.LCG(max=self.max_error_y_distance)
        for _ in range(tries):
            temp = math.sqrt(next(x_genrator) ** 2 + next(y_genrator) ** 2)
            if temp <= self.shield_rad:
                self.second_points.append(temp)
        return None
        
    def compare(self, with_mean=True):
        if with_mean:
            p = statistics.mean(np.subtract(self.first_points, self.second_points).tolist())
        else:
            p = np.subtract(self.first_points, self.second_points).tolist()
        # print(p)
        return p

    def simulate(self, simulation=20):
        temp = []
        for _ in range(simulation):
            self.first()
            self.second()
            temp.append(self.compare())
        print(temp)
        

if __name__ == "__main__":
    test = Archers()
    test.simulate()
