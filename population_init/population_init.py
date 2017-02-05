#!/usr/bin/env python
#encoding:UTF-8
import random

#种群初始化函数
def population_init(population, N, V, nbits):
    #自变量个数V并没有用到
    del population[:]
    for i in xrange(N):
        tempIndividual=[]
        for j in nbits:
            tempVal=[]
            for k in xrange(j):
                tempVal.append(random.randint(0, 1))
            tempIndividual.append(tempVal)
        population.append(tempIndividual)

#测试代码
if __name__=="__main__":
    population=[]
    N=200
    V=2
    nbits=(17, 17)
    population_init(population, N, V, nbits)
    print population
