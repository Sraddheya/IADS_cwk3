import math
import graph
import random
import timeit

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

def metricGraph(numNodes, maxDist):
    width_height = math.floor(maxDist * math.sin(math.radians(45)))
    euclideanGraph(numNodes, width_height, width_height)
    g = graph.Graph(-1, "euclideanGraph")
    writer = open('metricGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    for u in range(numNodes-1):
        for v in range(u+1, numNodes):
            writer.write(str(u) + " " + str(v) + " " + str(g.dist[u][v]) + "\n")
    writer.close()