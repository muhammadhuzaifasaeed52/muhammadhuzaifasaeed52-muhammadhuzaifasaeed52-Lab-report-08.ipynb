import heapq

def best_first_search(graph, h, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (h[start], start, [start]))
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neigh, cost in graph[node]:
                heapq.heappush(pq, (h[neigh], neigh, path + [neigh]))
    return None

def beam_search(graph, h, start, goal, k):
    frontier = [(start, [start])]
    while frontier:
        candidates = []
        for node, path in frontier:
            if node == goal:
                return path
            for neigh, cost in graph[node]:
                candidates.append((neigh, path + [neigh]))
        candidates.sort(key=lambda x: h[x[0]])
        frontier = candidates[:k]
    return None

def astar(graph, h, start, goal):
    pq = []
    heapq.heappush(pq, (h[start], 0, start, [start]))
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if node not in visited:
            visited.add(node)
            for neigh, cost in graph[node]:
                new_g = g + cost
                new_f = new_g + h[neigh]
                heapq.heappush(pq, (new_f, new_g, neigh, path + [neigh]))
    return None


graph_a = {
    'a': [('b', 9), ('c', 12), ('d', 7)],
    'b': [('a', 9), ('c', 14), ('e', 11)],
    'c': [('a', 12), ('b', 14), ('d', 18), ('f', 17)],
    'd': [('a', 7), ('c', 18), ('f', 14)],
    'e': [('b', 11), ('z', 5)],
    'f': [('c', 17), ('d', 14), ('z', 8)],
    'z': [('e', 5), ('f', 8)]
}

h_a = {
    'a': 21, 'b': 14, 'c': 12, 'd': 18,
    'e': 5, 'f': 9, 'z': 2
}

graph_b = {
    'S': [('A',4),('B',8),('C',11)],
    'A': [('S',4),('D',15)],
    'B': [('S',8),('D',5),('C',10)],
    'C': [('S',11),('B',10),('E',20),('F',13)],
    'D': [('A',15),('B',5),('H',16),('I',20),('F',1)],
    'E': [('C',20),('F',19)],
    'F': [('D',1),('C',13),('I',5),('G',13)],
    'H': [('D',16),('I',2)],
    'I': [('D',20),('H',2),('F',5),('J',5),('K',13)],
    'J': [('I',5)],
    'K': [('I',13),('G',16)],
    'G': [('F',13),('K',16)]
}

h_b = {
    'S':7,'A':8,'B':6,'C':5,'D':1,'E':3,'F':3,'G':0,
    'H':7,'I':4,'J':5,'K':3
}


print("Graph A – Best First:", best_first_search(graph_a, h_a, 'a', 'z'))
print("Graph A – Beam Search:", beam_search(graph_a, h_a, 'a', 'z', 2))

print("Graph B – Best First:", best_first_search(graph_b, h_b, 'S', 'G'))
print("Graph B – Beam Search:", beam_search(graph_b, h_b, 'S', 'G', 2))
print("Graph B – A* Search:", astar(graph_b, h_b, 'S', 'G'))
