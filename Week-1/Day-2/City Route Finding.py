from collections import deque

graph = {
    'A': [('B',5), ('C',8)],
    'B': [('D',3)],
    'C': [('D',2)],
    'D': [('E',4)],
    'E': []
}

def bfs(start, goal):
    q = deque([(start, [start], 0)])
    
    while q:
        node, path, dist = q.popleft()
        
        if node == goal:
            return path, dist
        
        for n, d in graph[node]:
            q.append((n, path+[n], dist+d))

route, distance = bfs('A','E')
print("Route:", " → ".join(route))
print("Distance:", distance, "km")

##########            Output              #########
Route: A → B → D → E
Distance: 12 km
