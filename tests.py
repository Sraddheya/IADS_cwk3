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

def printTest(g, n, filename):
    #Initial
    print("Initial: " + str(g.perm) + " " + str(g.tourValue()))

    #swapHeuristic
    time = timeit.timeit('g.swapHeuristic(' + str(g.n)+ ')', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.swapHeuristic(g.n)
    print("swapHeuristic: " + str(g.perm) + " " + str(g.tourValue()) + " " + str(time))

    #TwoOptHeuristic
    time = timeit.timeit('g.TwoOptHeuristic(' + str(g.n)+ ')', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.initPerm()
    g.TwoOptHeuristic(g.n)
    print("TwoOptHeuristic: " + str(g.perm) + " " + str(g.tourValue()) + " " + str(time))

    #Greedy
    time = timeit.timeit('g.Greedy()', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.initPerm()
    g.Greedy()
    print("Greedy: " + str(g.perm) + " " + str(g.tourValue()) + " " + str(time))

    if filename != 'nonMetricGraph':
        #Prim
        time = timeit.timeit('g.Prim()', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
        g.initPerm
        g.Prim()
        print("Prim: " + str(g.perm) + " " + str(g.tourValue()) + " " + str(time))

def euclideanTest(filename):
    if filename=="euclideanGraph":
        euclideanGraph(random.randint(3,20), random.randint(100,1000), random.randint(100,1000))
    g = graph.Graph(-1, filename)
    printTest(g, -1, filename)

def nonMetricTest():
    numNodes = random.randint(3,20)
    filename = 'nonMetricGraph'
    nonMetricGraph(numNodes, random.randint(1,100))
    g = graph.Graph(numNodes, filename)
    printTest(g, numNodes, filename)

def metricTest():
    numNodes = random.randint(3,20)
    filename = 'metricGraph'
    metricGraph(numNodes, random.randint(1,100))
    g = graph.Graph(numNodes, filename)
    printTest(g, numNodes, filename)
