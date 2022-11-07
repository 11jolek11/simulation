from generators.prand import LCG_CLS
import matplotlib.pyplot as plt
from collections import Counter
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

    print('Rozkład wyników')
    print("H0: Każdy gracz ma taką samą szansę na wygraną")
    print("HA: Każdy gracz ma różne szanse na wygraną")
    dataset = list(Counter(temp).values())
    labels = list(Counter(temp).keys())
    # print(labels)
    # print(Counter(temp))
    dist, pvalue = chisquare(dataset)
    uni = 'YES' if pvalue > 0.05 else 'NO'
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")
    if pvalue > 0.05: print("Różnice nie są wystarczająco znaczące przy alpha=0.05 przyjmujemy H0")
    else: print("Różnice nie są wystarczająco znaczące przy alpha=0.05 aby odrzucić H0")

    fig, ax = plt.subplots(1,1)
    # ax.hist(temp, bins=bins)
    bars = ax.bar(list(Counter(temp).keys()), list(Counter(temp).values()), width=1.0)
    ax.set_xticks(sorted(list(Counter(temp).keys())), labels=['Loss', 'Draws', 'Wins'])
    ax.bar_label(bars)
    # b = ax.bar(list(Counter(temp).keys()), list(Counter(temp).values()))
    # ax.bar_label(ax.containers[0])
    plt.tight_layout()
    plt.savefig('./images/kpn/kpn_hist.jpg')


def play():
    # 2 - win
    # 1 - draw
    # 0 - lost

    gen = LCG_CLS()
    # 1 - kamien
    # 2 - papier
    # 3 - nozyce
    first = [gen.uniform_int(1, 3) for _ in range(100)]
    second = [gen.uniform_int(1, 3) for _ in range(100)]
    # first = [gen.uniform_restricted(1, 3) for _ in range(100)]
    # second = [gen.uniform_restricted(1, 3) for _ in range(100)]

    # print('Rozklad rzutów drugiego gracza')
    # dataset = list(Counter(second).values())
    # print(Counter(second))
    # dist, pvalue = chisquare(dataset)
    # uni = 'YES' if pvalue > 0.05 else 'NO'
    # print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")

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
    generate_histogram(pl)
    # plt.hist(pl, bins=3)
    # plt.savefig('./test.jpg')



