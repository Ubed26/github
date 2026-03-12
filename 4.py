""" A) Write a program to implement Greedy Best First Search on a given graph. B) Write a program to implement A-star search on a given graph."""

#A) Greedy Best First Search (Python)
import heapq

def greedy_best_first(graph, heuristic, start, goal):

    visited = set()
    pq = [(heuristic[start], start, [start])]

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Path:", " -> ".join(path))
            return

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (heuristic[neighbour], neighbour, path + [neighbour]))


graph = {
    'P':[('R',4),('C',4),('A',4)],
    'R':[('E',5)],
    'C':[('R',2),('U',3),('M',6)],
    'A':[('M',3)],
    'M':[('U',5),('L',2)],
    'L':[('N',5)],
    'N':[('S',6)],
    'U':[('S',4),('N',5)],
    'E':[('S',1),('U',5)],
    'S':[]
}

heuristic = {
    'P':10,
    'R':8,
    'C':6,
    'A':11,
    'M':9,
    'L':9,
    'N':6,
    'U':4,
    'E':3,
    'S':0
}

print("Greedy Best First Search Path:")
greedy_best_first(graph,heuristic,'P','S')

#B) A* Search Algorithm (Python)

import heapq

def a_star(graph, heuristic, start, goal):

    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:

            g_new = g + cost
            f_new = g_new + heuristic[neighbour]

            heapq.heappush(pq,(f_new,g_new,neighbour,path+[neighbour]))


print("\nA* Search Result:")
a_star(graph,heuristic,'P','S')
