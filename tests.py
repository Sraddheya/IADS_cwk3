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

def printTest(g, n, opt, filename):
    #Initial
    print("Initial: " + str(g.perm) + " " + str(g.tourValue()))

    #swapHeuristic
    time = timeit.timeit('g.swapHeuristic(' + str(g.n)+ ')', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.swapHeuristic(g.n)
    swapTour = g.tourValue()
    print("swapHeuristic: " + str(g.perm) + " " + str(swapTour) + " " + str(time))

    #TwoOptHeuristic
    time = timeit.timeit('g.TwoOptHeuristic(' + str(g.n)+ ')', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.initPerm()
    g.TwoOptHeuristic(g.n)
    twoOptTour = g.tourValue()
    print("TwoOptHeuristic: " + str(g.perm) + " " + str(twoOptTour) + " " + str(time))

    #Greedy
    time = timeit.timeit('g.Greedy()', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.initPerm()
    g.Greedy()
    greedyTour = g.tourValue()
    print("Greedy: " + str(g.perm) + " " + str(greedyTour) + " " + str(time))

    if filename != 'nonMetricGraph':
        #Prim
        time = timeit.timeit('g.Prim()', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
        g.initPerm
        g.Prim()
        primTour = g.tourValue()
        print("Prim: " + str(g.perm) + " " + str(primTour) + " " + str(time))

    if opt > 0:
        approx = [swapTour, twoOptTour, greedyTour, primTour]
        approx = [round(i/opt, 2) for i in approx]
        print("How close to optimim: " + str(opt) + "? " + str(approx))

def euclideanTest(filename, opt):
    if filename=="euclideanGraph":
        euclideanGraph(random.randint(3,20), random.randint(100,1000), random.randint(100,1000))
    g = graph.Graph(-1, filename)
    printTest(g, -1, opt, filename)

def nonMetricTest():
    numNodes = random.randint(3,20)
    filename = 'nonMetricGraph'
    nonMetricGraph(numNodes, random.randint(1,100))
    g = graph.Graph(numNodes, filename)
    printTest(g, numNodes, -1, filename)

def metricTest():
    numNodes = random.randint(3,20)
    filename = 'metricGraph'
    metricGraph(numNodes, random.randint(1,100))
    g = graph.Graph(numNodes, filename)
    printTest(g, numNodes, -1, filename)
