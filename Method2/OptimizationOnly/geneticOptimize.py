# -*- coding:utf-8 -*-
import json
from random import randint, random

import buildModel


strList = {}


def func_using_abaqus(vector, count):
    if len(vector) == 4:
        res = buildModel.buildModel(vector[0], vector[1], vector[2], vector[3], count)
        return res
    else:
        return None


def combineVec(vector):
    s = ""
    for i in range(len(vector)):
        s += str(vector[i]) + "-"
    return s[:-1]


def costf(vector, f, count):
    """
    代价函数
    """
    strV = combineVec(vector)

    if strV in strList:
        y1= strList[strV]
    else:
        try:
            y1= f(vector, count)
        except:
            y1 = None
        strList[strV] = y1
        with open('data.json', 'wb') as f:
            json.dump(strList, f)
        
    if y1 is not None:
        return 1 / (y1 + 0.1)
    else:
        return None


def geneticoptimize(domain, costf, step, f, popsize=50, mutprob=0.2, elite=0.2, maxiter=30):
    """
    遗传算法
    """
    # Mutation Operation
    def mutate(vec):
        i = randint(0, len(domain) - 1)
        if random( ) < 0.5 and vec[i] > domain[i][0]:
            return vec[0:i] + [vec[i] - step[i]] + vec[i+1:]
        elif vec[i] < domain[i][1]:
            return vec[0:i] + [vec[i] + step[i]] + vec[i+1:]
        else:
            return None

    # Crossover Operation
    def crossover(r1,r2):
        i = randint(1, len(domain) - 2)
        return r1[0:i]+r2[i:]
    
    count = 0
    
    # Build the initial population
    pop=[]
    for i in range(popsize):
        vec = [round(randint(domain[i][0] / step[i], domain[i][1] / step[i]) * step[i], 1) for i in range(len(domain))]
        pop.append(vec)
    
    # How many winners from each generation?
    topelite = int(elite * popsize)
    
    # Main loop
    for i in range(maxiter):
        scores = []
        for v in pop:
            count += 1
            costVal = costf(v, f, count)
            if costVal is not None:
                scores.append((costVal, v))
        scores.sort( )
        ranked = [v for (s,v) in scores]
        
        # Start with the pure winners
        pop = ranked[0: topelite]
        
        # Add mutated and bred forms of the winners
        while len(pop) < popsize:
            if random( ) < mutprob:
                # Mutation
                c = randint(0, topelite - 1)
                tempVec = mutate(ranked[c])
                if tempVec is not None:
                    pop.append(tempVec)
            else:
                # Crossover
                c1 = randint(0, topelite - 1)
                c2 = randint(0, topelite - 1)
                pop.append(crossover(ranked[c1], ranked[c2]))
        
        # Print current best score
        print (scores[0][0])
    return scores[0][1]

    
def main():
    try:
        # 用来记录已经计算过的数据
        with open('data.json', 'rb') as f:
            strList = json.load(f)
    except:
        print ('no data.json')
    
    bestVec = geneticoptimize(
        domain=[(40.0,90.0),(0.8,1.5),(40.0,90.0), (1.5, 2.5)],
        costf=costf,
        step=[1.0, 0.1, 1.0, 0.1],
        f=func_using_abaqus,
        popsize=100,
        elite=0.3
        )
    print (bestVec)


if __name__ == '__main__':
    main()