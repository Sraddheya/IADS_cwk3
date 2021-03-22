import math
import graph
import random
import timeit

# Create a randomly generated euclidean graph and write into file 'euclideanGraph'
def euclideanGraph(numNodes, width, height):
    writer = open('euclideanGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    for u in range(numNodes):
        writer.write(str(random.randint(1, width)) + " " + str(random.randint(1, height)) + "\n")
    writer.close()

# Create a randomly generated non-Metric graph and write into file 'nonMetricGraph'
def nonMetricGraph(numNodes, maxDist):
    writer = open('nonMetricGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    for u in range(numNodes-1):
        for v in range(u+1, numNodes):
            writer.write(str(u) + " " + str(v) + " " + str(random.randint(1,maxDist)) + "\n")
    writer.close()

# Create a randomly generated metric graph and write into file 'metricGraph'
def metricGraph(numNodes, maxDist):
    width_height = math.floor(maxDist * math.sin(math.radians(45)))
    euclideanGraph(numNodes, width_height, width_height)
    g = graph.Graph(-1, "euclideanGraph")

    writer = open('metricGraph', 'w', encoding='utf-8')
    writer.truncate(0)
    for u in range(numNodes-1):
        for v in range(u+1, numNodes):
            writer.write(str(u) + " " + str(v) + " " + str(math.floor(g.dist[u][v])) + "\n")
    writer.close()

# Function that runs each algorithm on the same file and prints out the results
def printTest(g, n, opt, filename):
    #Initial
    print("Initial: " + str(g.perm) + " " + str(round(g.tourValue(), 2)))

    #swapHeuristic
    time = timeit.timeit('g.swapHeuristic(' + str(g.n)+ ')', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.swapHeuristic(g.n)
    swapTour = round(g.tourValue(), 3)
    print("swapHeuristic: " + str(g.perm) + " " + str(swapTour) + " " + str(time))

    #TwoOptHeuristic
    time = timeit.timeit('g.TwoOptHeuristic(' + str(g.n)+ ')', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.initPerm()
    g.TwoOptHeuristic(g.n)
    twoOptTour = round(g.tourValue(), 3)
    print("TwoOptHeuristic: " + str(g.perm) + " " + str(twoOptTour) + " " + str(time))

    #Greedy
    time = timeit.timeit('g.Greedy()', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
    g.Greedy()
    greedyTour = round(g.tourValue(), 3)
    print("Greedy: " + str(g.perm) + " " + str(greedyTour) + " " + str(time))

    # Prim will only work on graphs that follow the triangle inequality
    if filename != 'nonMetricGraph':
        #Prim
        time = timeit.timeit('g.Prim()', number = 1, setup = 'import graph\ng = graph.Graph(' + str(n) + ', "' + filename + '")')
        g.Prim()
        primTour = round(g.tourValue(), 3)
        print("Prim: " + str(g.perm) + " " + str(primTour) + " " + str(time))
        approx = [swapTour, twoOptTour, greedyTour, primTour]
    else:
        approx = [swapTour, twoOptTour, greedyTour]
    
    if opt > 0:
        approx = [round(i/opt, 2) for i in approx]
    else:
        minAlgo = min(approx)
        approx = [round(i/minAlgo, 2) for i in approx]
    print("How close to optimim: " + str(opt) + "? " + str(approx))

# Call PrintTest on randomly generated euclidean graph
def euclideanTest(filename, opt):
    if filename=="euclideanGraph":
        euclideanGraph(random.randint(3,50), random.randint(100,1000), random.randint(100,1000))
    g = graph.Graph(-1, filename)
    printTest(g, -1, opt, filename)

# Call PrintTest on randomly generated non-metric graph
def nonMetricTest():
    numNodes = random.randint(3,50)
    filename = 'nonMetricGraph'
    nonMetricGraph(numNodes, random.randint(1,100))
    g = graph.Graph(numNodes, filename)
    printTest(g, numNodes, -1, filename)

# Call PrintTest on randomly generated metric graph
def metricTest():
    numNodes = random.randint(3,50)
    filename = 'metricGraph'
    metricGraph(numNodes, random.randint(1,100))
    g = graph.Graph(numNodes, filename)
    printTest(g, numNodes, -1, filename)
