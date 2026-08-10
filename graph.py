from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = dict()


    def __repr__(self):
        graph_str = ""
        for node, neighbors in self.adjacency_list.items():
            graph_str += str(node) + " -> " + str(neighbors) + "\n"
        return graph_str


    def add_node(self, node):
        if not(node in self.adjacency_list):
            self.adjacency_list[node] = set()
        else:
            raise ValueError("Node already exists")


    def remove_node(self, node):
        if node not in self.adjacency_list:
            raise ValueError("Node does not exist")
        for neighbors in self.adjacency_list.values():
            neighbors.discard(node)
        del self.adjacency_list[node]


    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adjacency_list:
            self.add_node(from_node)
        if to_node not in self.adjacency_list:
            self.add_node(to_node)
        if weight is None:
            self.adjacency_list[from_node].add(to_node)
            if not self.directed:
                self.adjacency_list[to_node].add(from_node)
        else:
            self.adjacency_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adjacency_list[to_node].add((from_node, weight))


    def remove_edge(self, from_node, to_node):
        if from_node in self.adjacency_list:
            if to_node in self.adjacency_list[from_node]:
                self.adjacency_list[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exist")

            if not self.directed:
                if from_node not in self.adjacency_list[to_node]:
                    self.adjacency_list[to_node].remove(from_node)
        else:
            raise ValueError("Node does not exist")


    def get_neighbors(self, node):
        return self.adjacency_list.get(node, set())


    def has_node(self, node):
        return node in self.adjacency_list


    def has_edge(self, from_node, to_node):
        if from_node in self.adjacency_list:
            return to_node in self.adjacency_list[from_node]
        return False


    def get_nodes(self):
        return list(self.adjacency_list.keys())


    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adjacency_list.items():
            for to_node, weight in neighbors:
                edges.append((from_node, to_node))


    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order


    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order


if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 1)
    g.add_edge('A', 'E', 1)
    g.add_edge('E', 'F', 1)
    g.add_edge('G', 'F', 1)
    g.add_edge('F', 'H', 1)
    g.add_edge('H', 'I', 6)
    print(g)
