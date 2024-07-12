import heapq

def dijkstra(graph,start):
    pq = [(0,start)]

    visited = set()
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor,weight in graph[current_vertex]:
            d = current_distance + weight
            if d < distances[neighbor]:
                distances[neighbor] = d
                heapq.heappush(pq,(d,neighbor))
    return distances


if __name__ == '__main__':
    graph = {
        'A' : [('B',4),('C',2)],
        'B' : [('C',3),('D',2),('E',3)],
        'C' : [('B',1),('D',4),('E',5)],
        'D' : [('E',1)],
        'E' : []
    }
    print(dijkstra(graph,'A'))