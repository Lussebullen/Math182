import sys
input = sys.stdin.readline


def read_graph(n, k):
    edges = []
    for _ in range(k):
        i, j, r = input().split()
        edges.append((int(i), int(j), float(r)))
    return edges

def bellman_ford(n, k, edges, source):
    """
    :param n: Number of countries
    :param k: Number of given exchange rates
    :param edges: Edges as a tuple of vertex pairs and exchange rate
    :param source: Starting vertex
    :return: Is negative cycle reachable from source
    """
    dist = [sys.maxsize] * n
    dist[source - 1] = 0
    for i in range(n-1):
        for e in edges:
            dist[e[1] - 1] = min(dist[e[1] - 1], dist[e[0] - 1] * e[2])
    for e in edges:
        if dist[e[0] - 1] * e[2] < dist[e[1] - 1]:
            return True
    return False

def detect_cycle(n, k, edges):
    """
    :param n: number of countries
    :param k: number of exchange rates
    :param edges: Edges as a tuple of vertex pairs and exchange rate
    :return: Existence of negative cycle
    """
    for i in range(n):
        v = i + 1 # Vertex number
        if bellman_ford(n,k,edges,v):
            return True
    return False  # Replace with your solution


#TESTING
#IMPOSSIBLE
# n = 4
# k = 5
# edges = [
#     (1, 2, 2),
#     (1, 3, 1),
#     (2, 4, 3),
#     (4, 3, 0.5),
#     (3, 2, 0.75)]
# detect_cycle(n,k,edges)
# #POSSIBLE
# n2 = 5
# k2 = 4
# edges2 = [
#     (1, 2, 3),
#     (3, 4, 2),
#     (4, 5, 0.5),
#     (5, 3, 0.5)]
#
# detect_cycle(n2,k2,edges2)


# n = 10
# k = 14
# edges = [
# (8, 2, 3.0358689869769804),
# (2, 9, 2.025789275293564),
# (9, 8, 0.21916852762442965),
# (2, 7, 1.728818449925872),
# (1, 4, 6.280297426238624),
# (4, 3, 0.9952038366199136),
# (4, 6, 0.5309318996801742),
# (3, 4, 1.0293378914348454),
# (4, 8, 0.24225774027922287),
# (9, 4, 0.9740776851950621),
# (5, 6, 1.9428155270982292),
# (8, 1, 0.6571906742168461),
# (10, 1, 0.2551089784869654),
# (6, 7, 1.6096851739492466)]


for _ in range(int(input())):
     n = int(input())
     k = int(input())
     edges = read_graph(n, k)
     if detect_cycle(n, k, edges):
         print("possible")
     else:
         print("impossible")


# To run this code, type `python3 arbitrage.py < input.txt > output.txt`
# into the command line. To run it with small test cases that you type in by
# hand, simply run `python3 arbitrage.py` from the command line.