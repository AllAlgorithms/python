# Breadth First Search

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edges(self,_from,_to):
        for t in _to:
            self.graph[_from].append(t)

    def display(self):
        print self.graph

    def bfs(self,graph,start):
        queue = [start]
        visited = []

        while queue:
            a = queue.pop(0)
            if a not in visited:
                visited.append(a)
                for neighbor in graph[a]:
                    queue.append(neighbor)
        print visited

def main():

    G = Graph()
    G.add_edges(1,[2,7,8])
    G.add_edges(2,[3,6])
    G.add_edges(3,[4,5])
    G.add_edges(8,[9,12])
    G.add_edges(9,[10,11])
    G.display()
    G.bfs(G.graph,1)
    
if __name__ == '__main__':
    main()
