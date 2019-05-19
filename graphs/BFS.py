import collections


def bfs(graph, start):
    explored, queue = set(), [start]
    explored.add(start)
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.append(w)
    return explored


if __name__ == '__main__':
    G = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    print(bfs(G, 'A'))
