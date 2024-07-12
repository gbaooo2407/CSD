def dfs( graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next in graph[start]:
        if next not in visited:
            dfs(graph,next,visited)

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    dfs(graph,"A")