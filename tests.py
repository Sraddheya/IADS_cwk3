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

#w(u, v) ≤ w(u, x) + w(x, v)
#def metricGraph(numNodes, maxDist):
#    writer = open('metricGraph', 'w', encoding='utf-8')
#    writer.truncate(0)
#    dist = [[None for i in range(numNodes)] for j in range(numNodes)]
#    distance = random.randint(1,maxDist)
#    writeMetric(writer, dist, distance, 0, 1)
#    for u in range(2,numNodes):
#        distance = random.randint(1,maxDist)
#        writeMetric(writer, dist, distance, u, u-1)
#        for v in range(u-1):
#            distance = math.floor(math.sqrt(dist[u][u-1]*dist[u][u-1] + dist[u-1][v]*dist[v][u-1]))
#            if distance > maxDist:
#                distance = maxDist
#            writeMetric(writer, dist, distance, u, v)
#    writer.close()
#    isTriangle(dist, numNodes)

#def writeMetric(writer, dist, distance, u, v):
#    dist[u][v] = distance
#    dist[v][u] = distance
#    writer.write(str(u) + " " + str(v) + " " + str(distance) + "\n")

def isTriangle(dist, numNodes):
    for u in range(numNodes):
        for v in range(numNodes):
            if u!=v:
                for x in range(numNodes):
                    if x!= u and x!=v:
                        if dist[u][v]>dist[u][x]+dist[x][v]:
                            print(False)
                            print(str(u) + " " + str(x) + " " + str(v) + " " + str(dist[u][v]) + " " + str(dist[u][x]) + " " + str(dist[x][v]))
    print(True)