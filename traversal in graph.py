from collections import deque

n = int(input("Enter number of users: "))

graph = {}

for i in range(n):
    graph[i] = []

e = int(input("Enter number of connections: "))

print("Enter connections:")
for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting user: "))

visited = set()
queue = deque([start])

print("\nBFS Traversal:", end=" ")

while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

visited = set()

print("\nDFS Traversal:", end=" ")

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

dfs(start)
