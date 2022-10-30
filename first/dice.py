from first.generators.prand import Generators
from scipy import stats
import matplotlib.pyplot as plt
from numpy import random as ran
import numpy as np
from collections import Counter


class Game:
    def __init__(self) -> None:
        results = {}
        sum_enabled = True

    def player(self, games):
        generator = Generators.LCG(max=6)
        points = []
        for _ in range(games):
            points.append([next(generator), next(generator)])
        del generator
        return points

    def play(self, games=30, enable_sum=True):
        self.results = {"first": self.player(games), "second": self.player(games)}
        if enable_sum:
            self.sum_enabled  = True
            self.results["first"] = list(map(sum, self.results["first"]))
            self.results["second"] = list(map(sum, self.results["second"]))
        return self.results

    def histogram_plotter(self, player:str):
        if self.sum_enabled:
            plt.hist(self.results[player])
            plt.savefig('./' + player + '_hist.jpg')
        else:
            print("error")

    def wins_histogram_plotter(self, player:str):
        temp_results = self.results.copy()
        if not self.sum_enabled:
            print("error")
            return 0
        first_player = temp_results.pop(player)
        second_player = list(temp_results.values())
        temp_results = np.subtract(first_player, second_player).tolist()[0]
        print(temp_results)
        data = [x for x in temp_results if x > 0]

        plt.hist(data)
        plt.savefig("wins_of_" + player + "hist.jpg")
        


if __name__ == "__main__":
    game = Game()
    print(game.play())
    game.wins_histogram_plotter("first")
