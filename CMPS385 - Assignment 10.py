from collections import deque

class Graph:
    def __init__(self, vertices):
        self.graph = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming undirected graph

    def breadth_first_traversal(self, start):
        visited = set()
        queue = deque()

        print("Breadth First Traversal:")
        visited.add(start)
        queue.append(start)

        while queue:
            variable = queue.popleft()
            print(variable, end=' ')

            for neighbor in self.graph[variable]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()  # newline

    def depth_first_traversal(self, start):
        visited = set()
        stack = []

        print("Depth First Traversal:")
        visited.add(start)
        stack.append(start)

        while stack:
            variable = stack[-1]
            print(variable, end=' ')

            # Find an unvisited adjacent vertex
            found_unvisited = False
            for neighbor in self.graph[variable]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    found_unvisited = True
                    break

            if not found_unvisited:
                stack.pop()
        print()  # newline


# Example Usage
vertices = ['A', 'B', 'C', 'D', 'E']
g = Graph(vertices)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

g.breadth_first_traversal('A')
g.depth_first_traversal('A')