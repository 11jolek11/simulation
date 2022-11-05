from generators.prand import LCG
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


class Game:
    """
    Deprecated class don't use/read
    """
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
            plt.savefig('./images/dice/dice_' + player + '_hist.jpg')
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

class Dice:
    def __init__(self):
        self.generator = LCG()
        self.first_points = []
        self.second_points = []
        self.advanteges = []


    def roll_dice(self, n: int = 30):
        for _ in range(n):
            self.first_points.append( self.generator.uniform_restricted(1, 6) +  self.generator.uniform_restricted(1, 6))
            self.second_points.append( self.generator.uniform_restricted(1, 6) +  self.generator.uniform_restricted(1, 6))
        for i in range(len( self.first_points)):
             self.advanteges.append( self.first_points[i] -  self.second_points[i])

    def generate_histogram(self):
        fig, axs = plt.subplots(2)
        axs[0].set_title('Hitogram of First Player results')
        bins = range(2, 13)
        axs[0].hist(self.first_points, bins=bins, color='green')
        plt.xticks(bins)
        axs[0].set_xlabel("Results")
        axs[0].set_ylabel("Number of repetitions")


        axs[1].set_title('Hitogram of First Player advantages')
        bins = range(-10, 11)
        axs[1].hist(self.advanteges, bins=bins, color='red')
        plt.xticks(bins)
        axs[1].set_xlabel("Advantege")
        axs[1].set_ylabel("Number of repetitions")
        plt.tight_layout()
        print(len(self.first_points))
        print(len(self.advanteges))
        plt.savefig('./images/dice/hist_z3.jpg')
        

if __name__ == "__main__":
    p = Dice()
    p.roll_dice()
    p.generate_histogram()
    # game = Game()
    # print(game.play())
    # game.wins_histogram_plotter("first")
