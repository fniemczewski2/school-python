def dijkstra(graph):
    length = len(graph)
    nodes = [i for i in range(length)]

    visited = [0]
    nodes.remove(0)
    distance_graph = {0: 0}
    next = 0

    while nodes:
        distance = float('inf')
        for v in visited:
            for d in nodes:
                if graph[v][d]:
                    new_dist = graph[0][v] + graph[v][d]
                    if new_dist <= distance:
                        distance = new_dist
                        next = d
                        graph[0][d] = new_dist

        distance_graph[next] = distance

        visited.append(next)
        nodes.remove(next)

    return distance_graph


if __name__ == '__main__':
    graph_list = [[0, 2, None, 4, None, 1],
                  [1, 0, None, 2, 3, None],
                  [2, None, 0, 1, None, 4],
                  [None, None, 2, 0, 3, None],
                  [None, None, None, 4, 0, 1],
                  [3, None, 7, None, 1, 0]]

    distance = dijkstra(graph_list)

    print(distance)
