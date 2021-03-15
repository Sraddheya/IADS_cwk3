import math
import graph
import random

def euclideanGraph(numNodes, width, height):
    writer = open('euclideanGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    for u in range(numNodes):
        writer.write(str(random.randint(1, width)) + " " + str(random.randint(1, height)) + "\n")
    writer.close()

def nonMetricGraph(numNodes, maxDist):
    writer = open('nonMetricGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    for u in range(numNodes-1):
        for v in range(u+1, numNodes):
            writer.write(str(u) + " " + str(v) + " " + str(random.randint(1,maxDist)) + "\n")
    writer.close()

#w(u, v) ≤ w(u, x) + w(x, v)
def metricGraph(numNodes, maxDist):
    writer = open('metricGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    dist = [[0 for i in range(numNodes)] for j in range(numNodes)]
    for u in range(numNodes-1):
        for v in range(u+1, numNodes):
            if u == 0:
                distance = random.randint(1, maxDist)
            else:
                minDist = maxDist*2
                for x in range(u-1):
                    if dist[u][x] + dist[x][v] < minDist:
                        minDist = dist[u][x] + dist[x][v]
                distance = random.randint(1, minDist)
            dist[u][v] = distance
            dist[v][u] = distance
            writer.write(str(u) + " " + str(v) + " " + str(distance) + "\n")
    writer.close()