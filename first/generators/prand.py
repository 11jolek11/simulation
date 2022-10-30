from __future__ import annotations
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import chisquare
import math
import time



class LCG:
    def __init__(self) -> None:
        self.a=1103515245
        self.c=12345
        self.m=pow(2, 31)
        self.seed = 0

    def __seed(self):
        """Seed generator using system time"""
        time.sleep(0.001)
        self.seed = round(datetime.now().timestamp()*10009)

    def generate(self):
        self.__seed()
        return (self.a*self.seed + self.c) % self.m

    def uniform(self):
        return self.generate() / self.m

    def uniform_range(self, start: float, end: float):
        return (end - start) * self.uniform() + self.a
    
    def uniform_restricted(self, start: float, end: float):
        return math.floor(abs(1 + end - start) * self.uniform() + start)

    # def generate(self):
    #     while True:
    #         self.__seed()
    #         yield (self.a*self.seed + self.c) % self.m

    # def uniform(self):
    #     temp_generator = self.generate()
    #     while True:
    #         temp_value = next(temp_generator)
    #         yield temp_value/self.m

    # def unifrom_restricted(self, min:float, max: float) -> float:
    #     temp_uniform = self.uniform()
    #     while True:
    #         temp_value = next(temp_uniform)
    #         yield math.floor(abs(max - min + 1) * temp_value + min)



if __name__ == "__main__":
    p = LCG()
    # ucl = p.unifrom_restricted(1, 3)
    temp = []
    for _ in range(100):
        temp.append(p.uniform_restricted(1, 3))

    dataset = list(Counter(temp).values())

    plt.hist(temp, bins=3)
    plt.savefig('./test.jpg')

    dist, pvalue = chisquare(dataset)
    uni = 'YES' if pvalue > 0.05 else 'NO'
    print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")
    




    # dataset = []
    # x = Generators.LCG(max=1000000000000000000000)
    # for _ in range(3000):
    #     temp = next(x)
    #     # print(temp)
    #     dataset.append(temp)
    # plt.hist(dataset)
    # plt.savefig('./test.jpg')
    # plt.show()

    # # test = stats.kstest(dataset, stats.uniform(loc=0.0, scale=1000000000000000000000).cdf)
    # # print(test)
    # dataset = list(Counter(dataset).values())
    # # print(dataset)

    # dist, pvalue = chisquare(dataset)
    # uni = 'YES' if pvalue > 0.05 else 'NO'
    # print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")
