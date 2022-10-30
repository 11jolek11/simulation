from generators.prand import LCG
from scipy import stats
import matplotlib.pyplot as plt
from numpy import random as ran
from collections import Counter
from generators.prand import LCG
from scipy.stats import chisquare


def generate_histogram(data: dict):
    labels = list(data.keys())
    datagroups = list(data.values())
    bins = len(datagroups)

    fig, ax = plt.subplots(1, 1)
    ax.bar(labels, datagroups)
    plt.savefig('hist.jpg')


def play():
    # 2 - win
    # 1 - draw
    # 0 - lost
    result_table = {'wins': 0, 'draws': 0, 'loss': 0}

    gen = LCG()
    first = [gen.uniform_restricted(1, 3) for _ in range(100)]
    second = [gen.uniform_restricted(1, 3) for _ in range(100)]

    possible_output_matrix = [
#        first
#        k p   n
        [1, 2, 0], #k
        [0, 1, 2], # p second
        [2, 0, 1] # n
    ]

    dist, pvalue = chisquare(second)
    uni = 'YES' if pvalue > 0.05 else 'NO'
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")

    zipped = zip(first, second)

    for one, two in zipped:
        one = one - 1
        two = two - 1
        if possible_output_matrix[one][two] == 0:
            result_table['loss'] += 1
        if possible_output_matrix[one][two] == 1:
            result_table['draws'] += 1
        if possible_output_matrix[one][two] == 2:
            result_table['wins'] += 1
    return result_table


if __name__ == "__main__":
    pl = play()
    print(pl)
    # generate_histogram(pl)
    # plt.hist(pl, bins=3)
    # plt.savefig('./test.jpg')

    # pl = list(Counter(pl).values())
    # print(pl)

    # dist, pvalue = stats.chisquare(pl)
    # uni = 'YES' if pvalue > 0.05 else 'NO'
    # print(f"{dist:12.3f} {pvalue:12.8f} {uni}")

