class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        

class Infection(Graph):
    '''
    1. Simulate the spread of the disease using BFS (each level represents a new wave of infections).
    2. Identify individuals who are most likely to spread the disease (nodes with the highest degree).
    3. Find the shortest path (chain of transmission) between two individuals.
    '''
    def __init__(self):
        super().__init__()

    def bfs(self, start):
        visited = set()
        level = [0]
        queue = [start]
        visited.add(start)
        while queue:
            print(f'Level{level[0]}: {queue[0]}')
            lev = level[0]
            current = queue[0]
            level.pop(0)
            queue.pop(0)
            for edge in self.graph[current]:
                if edge not in visited:
                    level.append(lev + 1)
                    queue.append(edge)
                    visited.add(edge)
    
    def get_most_degree_person(self):
        maxvalue = -1
        maximum = ""
        for vertex in self.graph.keys():
            if len(self.graph[vertex]) > maxvalue:
                maxvalue = len(self.graph[vertex])
                maximum = vertex
        if maxvalue != -1:
            print(f'{maximum} is most likely to spread disease')

    def sortest_path_btw_two_indiv(self, fromVertex, toVertex):
        visited = set()
        queue = [fromVertex]
        visited.add(fromVertex)
        preds = {fromVertex: None}
        while queue:
            current = queue[0]
            queue.pop(0)
            if current == toVertex:
                break
            for edge in self.graph[current]:
                if edge not in visited:
                    queue.append(edge)
                    visited.add(edge)
                    preds[edge] = current
        path = []
        current = toVertex
        while current:
            path.append(current)
            current = preds[current]
        path = path[::-1]
        print(f'Shortest path between {fromVertex} and {toVertex}: {path}')