#!/usr/bin/env python
#encoding:UTF-8
from object_fun import object_fun

def eval_fun(population_real, xbin):
    del xbin[:]
    for i in population_real:
        xbin.append(object_fun(i))

