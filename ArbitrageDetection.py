import sys
input = sys.stdin.readline
import math

def read_graph(n, k):
    edges = []
    for _ in range(k):
        i, j, r = input().split()
        edges.append((int(i), int(j), float(r)))
    return edges

def bellman_ford_mod(n, k, edges):      #Floating point error when too many <1 multiplications
    """
    :param n: Number of countries
    :param k: Number of given exchange rates
    :param edges: Edges as a tuple of vertex pairs and exchange rate
    :param source: Starting vertex
    :return: Is there negative cycle
    """
    dist = [1] * n          #Start with ones as to avoid need of source, check from all points
    for i in range(n-1):    # Relax all edges for |V|-1 times
        for e in edges:
            dist[e[1] - 1] = min(dist[e[1] - 1], dist[e[0] - 1] * e[2])
    for e in edges:         #Check if relaxations still reduce distance, if so, "negative" cycle - arbitrage
        if dist[e[0] - 1] * e[2] < dist[e[1] - 1]:
            return True
    return False

def bellman_ford_mod2(n, k, edges):     #Same as above, but logarithmic to avoid floatingpoint errors.
    """
    :param n: Number of countries
    :param k: Number of given exchange rates
    :param edges: Edges as a tuple of vertex pairs and exchange rate
    :param source: Starting vertex
    :return: Is negative cycle reachable from source
    """
    dist = [0] * n          #All start at zero to imitate introduction of extra vertex with one way edge to all vertices
    for i in range(n-1):    #with weight zero - i.e. so it will find negative cycles regardles of start vertex.
        for e in edges:
            dist[e[1] - 1] = min(dist[e[1] - 1], dist[e[0] - 1] + math.log10(e[2]))
    for e in edges:
        if dist[e[0] - 1] + math.log10(e[2]) < dist[e[1] - 1]:
            return True
    return False

#For debugging and testing purposes
# with open('inputOriginal.txt') as f:
#     for _ in range(int(f.readline())):
#         n = int(f.readline())
#         k = int(f.readline())
#         edges = read_graph(n, k)
#         if bellman_ford_mod2(n, k, edges):
#             print("possible")
#         else:
#             print("impossible")

for _ in range(int(input())):
      n = int(input())
      k = int(input())
      edges = read_graph(n, k)
      if bellman_ford_mod2(n, k, edges):
          print("possible")
      else:
          print("impossible")


# To run this code, type `python3 arbitrage.py < input.txt > output.txt`
# into the command line. To run it with small test cases that you type in by
# hand, simply run `python3 arbitrage.py` from the command line.