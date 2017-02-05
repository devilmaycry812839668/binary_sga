#!/usr/bin/env python
#encoding:UTF-8
import random

def mutation(population, belta, nbits):
    for i in xrange(len(population)):
        for j in xrange(len(nbits)):
            for k in xrange(nbits[j]):
                r=random.random()
                if r<belta:
                    population[i][j][k]^=1


