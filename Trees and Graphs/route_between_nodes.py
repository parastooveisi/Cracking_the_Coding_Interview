def is_route(graph, start, end, visited):
    for node in graph[start]:
        if node not in visited:
            visited.append(node)
            if node == end or is_route(graph, node, end, visited):
                return True
    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"],
    "P": ["Q", "R"],
    "Q": ["P", "R"],
    "R": ["P", "Q"],
}


print(is_route(graph, "G", "B", []))
