# Explanation: https://www.askpython.com/python/examples/depth-first-search-algorithm


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited)
    return visited


# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        top = queue.pop()
        for n in graph[top]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return visited


graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}

print(dfs(graph, 'A', []))
print(bfs(graph, 'A'))
