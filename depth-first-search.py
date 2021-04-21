graph1 = {
    "A":["B","D"],
    "B":["A","C"],
    "H":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "C":["G","F"]
}
 
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph,k, visited)
    return visited
 
visited = dfs(graph1,'A', [])
print(visited)
