import math
import random

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        reader = open(filename,'r',encoding='utf-8')
        numLines = sum(1 for line in reader)
        reader.seek(0)
        if n<0:
            self.n = numLines
        else:
            self.n = n
        self.dist = [[0 for i in range(self.n)] for j in range(self.n)]
        self.perm = [0 for i in range(self.n)]

        if self.n!=n:
            line = reader.readlines()
            node = [s.split() for s in line]
            node = [[int(s[0]), int(s[1])] for s in node]
            for i in range(self.n):
                point1 = node[i]
                for j in range(i, self.n):
                    distance = 0
                    if i!=j:
                        point2 = node[j]
                        distance = euclid(point1, point2)
                    self.dist[i][j] = distance
                    self.dist[j][i] = distance
        else:
            for i in range(numLines):
               line = reader.readline()
               numbers = [int(s) for s in line.split()]
               self.dist[numbers[0]][numbers[1]] = numbers[2]
               self.dist[numbers[1]][numbers[0]] = numbers[2]

        self.initPerm()
        reader.close()

    # Helper function to initialise self.perm (mostly seperated for 
    # testing puposes)
    def initPerm(self):
        for i in range(self.n):
            self.perm[i] = i

    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        val = 0
        for i in range(self.n-1):
            val += self.dist[self.perm[i]][self.perm[i+1]]
        val += self.dist[self.perm[0]][self.perm[self.n-1]]
        return val

    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        origVal = self.tourValue()
        origPerm = self.perm[i]
        self.perm[i] = self.perm[(i+1)%self.n]
        self.perm[(i+1)%self.n] = origPerm
        if origVal<=self.tourValue():
            self.perm[(i+1)%self.n] = self.perm[i]
            self.perm[i] = origPerm
            return False
        else:
            return True

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):
        origVal = self.tourValue()
        revPerm = self.perm[i:j]
        revPerm.reverse()
        self.perm[i:j] = revPerm
        if origVal<=self.tourValue():
            revPerm.reverse()
            self.perm[i:j] = revPerm
            return False
        else:
            return True

    def swapHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                   better = True

    def TwoOptHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
                        
    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        used = [0]*self.n
        curNode = 0
        for i in range(self.n-1):
            min = max(self.dist[curNode])
            for j in range(self.n):
                if self.dist[curNode][j]<min and self.dist[curNode][j]!=0 and not(j in used):
                    min = self.dist[curNode][j]
                    used[i+1] = j
            curNode = used[i+1]
        self.perm = used

    # Own algorithm implementation taken from pseudocode in CLRS
    def Prim(self):
        maxWeight = max(max(x) for x in self.dist)+1
        weight = [maxWeight]*self.n
        used = [0]
        notUsed = self.perm
        notUsed.remove(0)
        while len(used)!=self.n:
            for v in notUsed:
                for u in used:
                    if self.dist[u][v] < weight[v] and u!=v:
                        weight[v] = self.dist[u][v]
            uIndex = weight.index(min(weight))
            notUsed.remove(uIndex)
            used.append(uIndex)
            weight[uIndex] = maxWeight
        self.perm = used