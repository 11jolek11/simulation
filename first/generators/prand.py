from __future__ import annotations
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import chisquare
import math
import time


# class LCG:
#     def __init__(self) -> None:
#         self.a=1103515245
#         self.c=12345
#         self.m=pow(2, 31)
#         self.seed = 0

#     def __seed(self):
#         """Seed generator using system time"""
#         self.seed = round(datetime.now().timestamp()*10009)
#         # print("Generating seed ..." + str(self.seed))

#     def generate(self):
#         self.__seed()
#         time.sleep(0.001)
#         # print(self.seed)
#         return (self.a*self.seed + self.c) % self.m

#     def uniform(self):
#         temp = self.generate() / self.m
#         return temp

#     def uniform_range(self, start: float, end: float):
#         # generates random float
#         temp = (end - start) * self.uniform() + start
#         print(str(temp) + " <" + str(self.seed) + ">")
#         return temp
    
#     def uniform_restricted(self, start: float, end: float):
#         # Generates random int value
#         temp = math.floor(abs(1 + end - start) * self.uniform() + start)
#         # print(str(temp) + " <" + str(self.seed) + ">")
#         return temp


class LCG_CLS:
    "LCG generator implemented using classmethods"
    seed = int(datetime.now().timestamp() * 10003)
    x = seed
    a = 22695477
    c = 1
    m = 2 ** 32

    @classmethod
    def _seed(cls, seed: int) -> None:
        # set_seed
        cls.seed = seed
        cls.x = seed

    @classmethod
    def generate(cls) -> int:
        # random
        cls.x = (cls.a * cls.x + cls.c) % cls.m
        return cls.x

    @classmethod
    def uniform(cls) -> float:
        # uniform
        # [0, 1)
        return cls.generate() / cls.m

    @classmethod
    def uniform_range(cls, a: float, b: float) -> float:
        # uniform_range
        # [a, b)
        return (b - a) * cls.uniform() + a

    @classmethod
    def uniform_int(cls, a: int, b: int) -> int:
        # randint
        # [a, b]
        # cls._seed(datetime.now().timestamp() * 10003)
        # temp = ((cls.a * cls.x + cls.c) % cls.m) / cls.m
        # return int(math.floor(b * temp) + a)
        return math.floor(abs(b - a + 1) * cls.uniform() + a)





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
    dataset = []
    for _ in range(800):
        dataset.append(LCG_CLS().uniform_int(1, 5))

    print(dataset)

    distribution = list(Counter(dataset).values())
    dist, pvalue = chisquare(distribution)
    uni = '\033[92mYES\033[0m' if pvalue > 0.05 else '\033[91mNO \033[0m'
    print('-----------------------------------------------------------')
    print(f"| Value:{dist:12.3f} | p-value: {pvalue:12.8f} Uniform: {uni:^8} |")
    print('-----------------------------------------------------------')































    # temp = []
    # for _ in range(100):
    #     temp.append(p.uniform_restricted(1, 3))

    # dataset = list(Counter(temp).values())

    # plt.hist(temp, bins=3)
    # plt.savefig('./test.jpg')

    # dist, pvalue = chisquare(dataset)
    # uni = 'YES' if pvalue > 0.05 else 'NO'
    # print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8}")

    # x = []
    # y = []
    # for _ in range(100):
    #     x.append(p.uniform_restricted(1, 1000))

    # for _ in range(100):
    #     y.append(p.uniform_restricted(1, 1000))

    # plt.scatter(x, y)
    # plt.savefig('gen_scatter.jpg')
    




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
