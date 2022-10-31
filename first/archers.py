from generators.prand import LCG
from scipy import stats
import matplotlib.pyplot as plt
from numpy import random as ran
import numpy as np
from collections import Counter
import math
import statistics
from time import sleep, time
from scipy.stats import chisquare

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
        

def archery(rounds: int = 10, size: int = 1220) -> dict:
    debug_x = []
    debug_y = []
    archer1_data = {'scores': [], 'points': [], 'distances': []}
    archer2_data = {'scores': [], 'points': [], 'distances': []}
    for _ in range(rounds):
        p = LCG()
        archer1_score, archer2_score = 0, 0
        radius = size * 0.5

        # archer1
        # dist = p.uniform_restricted(-1000, 1000)  # (0, 1000)
        # angle = p.uniform_range(0, 2 * math.pi)
        # x, y = dist * math.cos(angle), dist * math.sin(angle)


        # FIXME: PUNKTY X I Y UKLADAJA SIE W LINIE PROSTA
        _x = p.uniform_range(0, 122)
        _y = p.uniform_range(0, 122)
        debug_x.append(_x)
        debug_y.append(_y)
        dist = math.sqrt(_x ** 2 + _y ** 2)
        archer1_score += 1 if abs(dist) <= radius else 0

        archer1_data['points'].append((_x, _y))
        archer1_data['scores'].append(archer1_score)
        archer1_data['distances'].append(dist)

        # archer2
        # FIXME: PUNKTY X I Y UKLADAJA SIE W LINIE PROSTA
        x = p.uniform_restricted(-900, 900)

        y = p.uniform_restricted(-900, 900)

        debug_x.append(x)
        debug_y.append(y)
        dist = math.sqrt(x ** 2 + y ** 2)
        archer2_score += 1 if dist <= radius else 0

        archer2_data['points'].append((x, y))
        archer2_data['scores'].append(archer2_score)
        archer2_data['distances'].append(dist)

    archers_data = {'archer1': archer1_data, 'archer2': archer2_data}

    dataset = list(Counter(debug_x).values())

    # dist, pvalue = chisquare(dataset)
    # uni = 'YES' if pvalue > 0.05 else 'NO'
    # print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")

    plt.scatter(debug_x, debug_y)
    plt.savefig('archers_deb.jpg')

    return archers_data


if __name__ == '__main__':
    import numpy as np

    fig, ax = plt.subplots()
    points_archer1 = []
    points_archer2 = []
    dists_archer1 = []
    dists_archer2 = []
    score_archer1 = 0
    score_archer2 = 0
    for _ in range(20):
        result = archery()
        dists_archer1 += result['archer1']['distances']
        dists_archer2 += result['archer2']['distances']
        points_archer1 += result['archer2']['points']
        points_archer2 += result['archer1']['points']
        score_archer1 += sum(result['archer1']['scores'])
        score_archer2 += sum(result['archer2']['scores'])

    print(sum(dists_archer2) / len(dists_archer2))  # 500 * sqrt(2)
    print(sum(dists_archer1) / len(dists_archer1))  # 500
    print('---')
    print(score_archer1, score_archer2)

    ax.scatter(*zip(*points_archer2), alpha=0.5)
    ax.scatter(*zip(*points_archer1), alpha=0.5)
    ax.set_xticks(np.arange(-1000, 1001, 250))
    ax.set_yticks(np.arange(-1000, 1001, 250))
    target = plt.Circle((0, 0), 660, color='green', fill=False, linewidth=2.5)
    ax.add_patch(target)
    ax.set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.savefig('archers_scatter_debug.jpg')

























    # test = Archers()
    # test.simulate()
    # fig, ax = plt.subplots()
    # points_archer1 = []
    # points_archer2 = []
    # dists_archer1 = []
    # dists_archer2 = []
    # score_archer1 = 0
    # score_archer2 = 0
    # for _ in range(20):
    #     result = archery()
    #     dists_archer1 += result['archer1']['distances']
    #     dists_archer2 += result['archer2']['distances']
    #     points_archer1 += result['archer2']['points']
    #     points_archer2 += result['archer1']['points']
    #     score_archer1 += sum(result['archer1']['scores'])
    #     score_archer2 += sum(result['archer2']['scores'])

    # print(sum(dists_archer2) / len(dists_archer2))  # 500 * sqrt(2)
    # print(sum(dists_archer1) / len(dists_archer1))  # 500
    # print('---')
    # print(score_archer1, score_archer2)

    # ax.scatter(*zip(*points_archer2))
    # ax.scatter(*zip(*points_archer1))
    # ax.set_xticks(np.arange(-1000, 1001, 250))
    # ax.set_yticks(np.arange(-1000, 1001, 250))
    # target = plt.Circle((0, 0), 660, color='green', fill=False, linewidth=2.5)
    # ax.add_patch(target)
    # ax.set_aspect('equal', adjustable='box')
    # plt.tight_layout()
    # plt.savefig('z4.jpg')
