# defining a new class
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # edges adding
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # results printing
    def print_distance(self, distance):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, distance[i]))

    def bellman_ford(self, src):

        # setting all distances as infinity
        dist = [float("Inf")] * self.V
        # setting distances to starting point as 0
        dist[src] = 0

        # main function, searching for the shortest path
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # searching for negative cycle
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.print_distance(dist)


# nodes defining
# edge = (starting point, end point, weight)
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
g.bellman_ford(0)
