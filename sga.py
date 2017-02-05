#!/usr/bin/env python
#encoding:UTF-8
import random
from population_init.population_init import population_init
from decode.decode import decode
from function.eval_fun import eval_fun
from selection.selection import selection
from crossover.crossover import crossover
from mutation.mutation import mutation

N=200
V=2
nbits=(17, 17)
minBinVal=(-5, -5)
maxBinVal=(5, 5)
population=[]
population_real=[]
alfa=0.9
belta=0.05

#目标函数值列表
xbin=[]


def per_run():
    population_init(population, N, V, nbits)

    for i in xrange(200):
        decode(population, population_real, minBinVal, maxBinVal, nbits)
        eval_fun(population_real, xbin)
        selection(population, xbin)
        crossover(population, alfa, nbits)
        mutation(population, belta, nbits)

    decode(population, population_real, minBinVal, maxBinVal, nbits)
    eval_fun(population_real, xbin)
    return 100.0-max(xbin)


if __name__=="__main__":
    score_list=[]
    for i in xrange(100):
        temp=per_run()
        score_list.append(temp)
        print i, " : ", temp
    print sum(score_list)/len(score_list)


