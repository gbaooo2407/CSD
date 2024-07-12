class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dictionary: ",self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)

        return paths


if __name__ == '__main__':
    routes = {
        ("HCM","VT"),
        ("HCM","DL"),
        ("VT","HN"),
        ("DL","VT"),
        ("DL","NT"),
    }

    start = "HCM"
    end = "HN"
    routes_graph = Graph(routes)

    print(f"All paths from {start} to {end}: ",routes_graph.get_paths(start,end))