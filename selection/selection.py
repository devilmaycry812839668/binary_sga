#!/usr/bin/env python
#encoding:UTF-8
import copy
import random
#轮盘赌选择法
def selection(population, xbin):
    s=sum(xbin)
    temp=[k*1.0/s for k in xbin]
    temp2=[]

    s2=0
    for k in temp:
        s2=s2+k
        temp2.append(s2)

    temp3=[]
    for _ in xrange(len(population)):
        r=random.random()
        for i in xrange(len(temp2)):
            if r<=temp2[i]:
                temp3.append(i)
                break

    temp4=[]
    temp5=[]
    for i in temp3:
        temp4.append(copy.deepcopy(population[i]))
        temp5.append(xbin[i])
    population[:]=temp4
    xbin[:]=temp5

#测试代码
#selection(population, xbin)


