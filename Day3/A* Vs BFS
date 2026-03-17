import random
import heapq
import time
from collections import deque
SIZE=10
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for _ in range(20):
    x = random.randint(0, SIZE-1)
    y = random.randint(0, SIZE-1)
    grid[x][y] = 1

start = (0,0)
goal = (9,9)
grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0
def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def bfs(grid,start,goal):

    queue = deque([start])
    visited = set([start])
    parent = {}
    explored = 0
    
    while queue:
        current = queue.popleft()
        explored += 1

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, explored

        x,y = current

        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx,ny in neighbors:
            if 0<=nx<SIZE and 0<=ny<SIZE:

                if grid[nx][ny] == 1:
                    continue

                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny))
                    parent[(nx,ny)] = current
    return None, explored
def astar(grid,start,goal):

    open_set = []
    heapq.heappush(open_set,(0,start))
    came_from = {}
    g_score = {start:0}
    explored = 0
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        explored += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, explored

        x,y = current

        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx,ny in neighbors:
            if 0<=nx<SIZE and 0<=ny<SIZE:
                if grid[nx][ny] == 1:
                    continue
                new_g = g_score[current] + 1

                if (nx,ny) not in g_score or new_g < g_score[(nx,ny)]:
                    g_score[(nx,ny)] = new_g
                    f = new_g + heuristic((nx,ny),goal)
                    heapq.heappush(open_set,(f,(nx,ny)))
                    came_from[(nx,ny)] = current

    return None, explored
start_time = time.time()
bfs_path, bfs_nodes = bfs(grid,start,goal)
bfs_time = time.time() - start_time
start_time = time.time()
astar_path, astar_nodes = astar(grid,start,goal)
astar_time = time.time() - start_time
print("BFS Path Length =", len(bfs_path)-1)
print("BFS Nodes Explored =", bfs_nodes)
print("BFS Runtime =", bfs_time)

print()

print("A* Path Length =", len(astar_path)-1)
print("A* Nodes Explored =", astar_nodes)
print("A* Runtime =", astar_time)

########                OUTPUT                ########
BFS Path Length = 18
BFS Nodes Explored = 80
BFS Runtime = 0.00021791458129882812

A* Path Length = 18
A* Nodes Explored = 75
A* Runtime = 0.0004107952117919922
  
