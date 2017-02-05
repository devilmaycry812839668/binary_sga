#!/usr/bin/env python
#encoding:UTF-8

#种群个体解码
def decode(population, population_real, minBinVal, maxBinVal, nbits):
    del population_real[:]

    def iner(valList):
        L=len(valList)
        s=0
        for i in valList:
            s=s+i*(2**(L-1))
            L=L-1
        return s

    for i in population:
        temp=[]
        for j in i:
            temp.append(iner(j))

        for j in xrange(len(temp)):
            temp[j]=temp[j]*(maxBinVal[j]-minBinVal[j])*1.0/(2**(nbits[j])-1)+minBinVal[j]
        population_real.append(temp)



