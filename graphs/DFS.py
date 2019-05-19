def dfs(graph, start):
    explored, stack = set(), [start]
    explored.add(start)
    while stack:
        v = stack.pop()
        print(v, 'v')
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                stack.append(w)
                print(w)
    return explored


if __name__ == '__main__':
    G = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    print(dfs(G, 'A'))
