from collections import deque

def bfs(graph,start,visited = None):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end = " ")
        for next in graph[vertex]:
            if next not in visited:
                visited.add(next)
                queue.append(next)


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    bfs(graph, "A")
