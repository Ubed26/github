"""Write a program to implement Uniform cost search algorithm on a given graph. Consider the given graph is undirected."""

import heapq

def uniform_cost_search(graph, start, goal):

    visited = set()
    pq = [(0, start, [start])]   # (cost, node, path)

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (cost + weight, neighbour, path + [neighbour]))

    print("No path found")


# Undirected graph representation
graph = {
    'A': [('B',2), ('C',4)],
    'B': [('A',2), ('E',3), ('D',3)],
    'C': [('A',4), ('F',5)],
    'D': [('B',3), ('G',2)],
    'E': [('B',3), ('G',1)],
    'F': [('C',5), ('G',2)],
    'G': [('D',2), ('E',1), ('F',2)]
}

start = 'S'  # change according to your graph
goal = 'R'

uniform_cost_search(graph, start, goal)
