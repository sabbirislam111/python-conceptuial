
from queue import Queue
class Graph:
    def __init__(self, num_of_nodes, directed = False):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.adj_matrix = [[0 for col in range(self.num_of_nodes)] for row in range(self.num_of_nodes)]
        self.adj_list = {node:set() for node in range(self.num_of_nodes)}
        # print(self.adj_list)
        # print(self.adj_matrix)

    def add_node_adj_list(self, node1, node2):
        self.adj_list[node1].add(node2)
        if not self.directed: # bidirectional list
            self.adj_list[node1].add(node2)
    
    def add_node_adj_matrix(self, node1, node2):
        self.adj_matrix[node1][node2] = 1
        if not self.directed: # bidirectional matrix
            self.adj_matrix[node1][node2] = 1


    def bfs_teaversal(self, root):
        viseted = set()
        queue = Queue()
        queue.put(root)
        viseted.add(root)
        while not queue.empty():
            current_node = queue.get()
            print(current_node)
            for child in self.adj_list[current_node]:
                if child not in viseted:
                    queue.put(child)
                    viseted.add(child)

    visited = set()
    def dfs_traversal(self, root):
        if root not in self.visited:
            print(root)
            self.visited.add(root)
            for child in self.adj_list[root]:
                self.dfs_traversal(child)


m = Graph(5, True)
m.add_node_adj_list(0, 1)
m.add_node_adj_list(0, 2)
m.add_node_adj_list(1, 3)
m.add_node_adj_list(2, 4)


# m.add_node_adj_matrix(0, 1)
# m.add_node_adj_matrix(0, 2)
# m.add_node_adj_matrix(1, 0)
# m.add_node_adj_matrix(1, 2)
# m.add_node_adj_matrix(2, 1)

# print(m.adj_list)
# print(m.adj_matrix)

# m.bfs_teaversal(0)
m.dfs_traversal(0)

