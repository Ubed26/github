""" A) Write a program to implement BFS approach on a given graph. B) Write a program to implement DFS approach on the given graph. C) Write a program to solve the 2-water jug problem by Breadth First Search Approach."""

#A) Breadth First Search (BFS) on a Graph

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    'A': ['B','D'],
    'B': ['A','C','E'],
    'C': ['B'],
    'D': ['A'],
    'E': ['B']
}

print("BFS Traversal:")
bfs(graph,'A')

#B) Depth First Search (DFS) on a Graph

def dfs(graph, node, visited):
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


graph = {
    'A': ['B','D'],
    'B': ['A','C','E'],
    'C': ['B'],
    'D': ['A'],
    'E': ['B']
}

visited = set()

print("DFS Traversal:")
dfs(graph,'A',visited)

#C) Water Jug Problem using BFS

from collections import deque

def water_jug_bfs(cap1, cap2, target):

    visited = set()
    queue = deque([(0,0)])

    while queue:

        x,y = queue.popleft()

        if (x,y) in visited:
            continue

        print(x,y)

        visited.add((x,y))

        if x == target or y == target:
            print("Target reached")
            return

        next_states = [
            (cap1,y),      # fill jug1
            (x,cap2),      # fill jug2
            (0,y),         # empty jug1
            (x,0),         # empty jug2
            (x-min(x,cap2-y), y+min(x,cap2-y)),  # pour jug1->jug2
            (x+min(y,cap1-x), y-min(y,cap1-x))   # pour jug2->jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)


water_jug_bfs(4,3,2)
