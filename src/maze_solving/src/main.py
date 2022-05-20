from collections import deque


# printing maze
maze = open('../files/maze.txt')
print(maze.read())


# solving maze
# function defining
def solving(maze):

    # columns and rows counting
    Y, X = len(maze), len(maze[0])
    print("\nn of columns: ", X)
    print("n of rows: ", Y)
    # searching for start point
    for y in range(Y):
        for x in range(X):
            if maze[y][x] == 'S':
                # setting maze start point
                start = (y, x)
                print("\nstart point: ", [x, y])
                break
        else:
            continue
        break
    else:
        # no start point in the maze
        return None

    queue = deque()
    queue.append((start[0], start[1], 0, [start[0] * X + start[1]]))
    # move directions defining
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # setting all as non-visited
    visited = [[False] * X for _ in range(Y)]

    while len(queue) != 0:
        # testing another possible way - next from the stack
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        # exit searching
        if maze[coord[0]][coord[1]] == "E":
            print ("end point: ", [coord[1],coord[0]])
            return coord[2], [[i//X, i % X] for i in coord[3]]

        # path searching
        for n in directions:
            # defining neighbours
            ny, nx = coord[0] + n[0], coord[1] + n[1]
            # testing if neighbour a wall or visited or out of the maze
            # print(ny, nx)
            if ny < 0 or ny >= Y or nx < 0 or nx >= X or maze[ny][nx] == "X" or visited[ny][nx]:
                continue

            queue.appendleft((ny, nx, coord[2] + 1, coord[3] + [ny * X + nx]))


# analysing file with maze
with open("../files/maze.txt") as f:
    maze = []
    for line in f:
        maze.append([i for i in line.strip("\n")])
    pathLen, pathItems = solving(maze)
    print("\npath length:", pathLen)
    print("path items:", *pathItems)
