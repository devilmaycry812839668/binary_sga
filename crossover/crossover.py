#!/usr/bin/env python
#encoding:UTF-8

#二进制编码,单点交叉
def crossover(population, alfa, nbits):
    for i in xrange(len(population), 2):
        for j in xrange(len(nbits)):
            r=random.random()
            if r<alfa:
                p=random.randint(1, nbits[j]-1)
                population[i][j][p:], population[i+1][j][p:]=population[i+1][j][p:], population[i][j][p:]



