from generators.prand import LCG
import matplotlib.pyplot as plt
from collections import Counter
from generators.prand import LCG
from scipy.stats import chisquare


possible_output_matrix = [
#        first
#        k p   n
        [1, 2, 0], #k
        [0, 1, 2], # p second
        [2, 0, 1] # n
    ]


def generate_histogram(zipped: zip):
    temp = []

    for one, two in zipped:
        one = one - 1
        two = two - 1
        temp.append(possible_output_matrix[one][two])

    dataset = list(Counter(temp).values())
    print(Counter(temp))
    dist, pvalue = chisquare(dataset)
    uni = 'YES' if pvalue > 0.05 else 'NO'
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")

    fig, ax = plt.subplots(1, 1)
    bins=[0, 1, 2, 3]
    ax.hist(temp, bins = bins)
    plt.xticks(bins)
    plt.xlabel('Loss Draws Wins')
    plt.savefig('hist.jpg')


def play():
    # 2 - win
    # 1 - draw
    # 0 - lost

    gen = LCG()
    first = [gen.uniform_restricted(1, 3) for _ in range(100)]
    second = [gen.uniform_restricted(1, 3) for _ in range(100)]

    dataset = list(Counter(second).values())
    dist, pvalue = chisquare(dataset)
    uni = 'YES' if pvalue > 0.05 else 'NO'
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")

    zipped = zip(first, second)
    # print(zipped)

    # for one, two in zipped:
    #     one = one - 1
    #     two = two - 1
    #     if possible_output_matrix[one][two] == 0:
    #         result_table['loss'] += 1
    #     if possible_output_matrix[one][two] == 1:
    #         result_table['draws'] += 1
    #     if possible_output_matrix[one][two] == 2:
    #         result_table['wins'] += 1
    # return result_table
    return zipped


if __name__ == "__main__":
    pl = play()
    print(pl)
    generate_histogram(pl)
    # plt.hist(pl, bins=3)
    # plt.savefig('./test.jpg')



