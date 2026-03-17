from collections import deque
grid = [
    ['W', '.', '.', 'X', 'C'],
    ['.', 'X', '.', 'X', '.'],
    ['.', '.', '.', '.', 'A'],
    ['X', '.', 'X', '.', '.'],
    ['D', '.', '.', 'B', '.']
]
warehouse = (0, 0)
deliveries = {
    'A': (2, 4),
    'B': (4, 3),
    'C': (0, 4),
    'D': (4, 0)
}
rows = len(grid)
cols = len(grid[0])
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        visited.add((x, y))

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] != 'X' and
                (nx, ny) not in visited):

                queue.append(((nx, ny), path + [(nx, ny)]))

    return None
total_distance = 0
for point, location in deliveries.items():
    path = bfs(warehouse, location)

    if path:
        distance = len(path) - 1
        total_distance += distance
        print(f"W → {point}: {path}")
        print("Distance:", distance)

print("Total Delivery Distance:", total_distance)

########              OUTPUT              ########
W → A: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
Distance: 6
W → B: [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)]
Distance: 7
W → C: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4)]
Distance: 8
W → D: [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 0)]
Distance: 6
Total Delivery Distance: 54
