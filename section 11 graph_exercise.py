class Graph_undirected_unweighted:
    def __init__(self):
        self.data = {}
        self.nodes = 0
    
    def add_vertex(self,node):
        if not self.data.get(node):
            self.data[node]=set()
            self.nodes+=1
    
    def add_edge(self,node1,node2):
        if not (node1 and node2):
            return
        if self.data.get(node1):
            self.data[node1].add(node2)
        else:
            self.data[node1]=set()
            self.data[node1].add(node2)
            self.nodes+=1
        if self.data.get(node2):
            self.data[node2].add(node1)
        else:
            self.data[node2]=set()
            self.data[node2].add(node1)
            self.nodes+=1
    
    def show_connections(self):
        items = list(self.data.keys())
        items.sort()
        for item in items:
            print(f'{item} -->',*self.data.get(item))

from random import randint

test = Graph_undirected_unweighted()

for i in range(10):
    test.add_vertex(i)
test.show_connections()

max=50
min=10
for i in range(10):
    val1, val2 = randint(min,max), randint(min,max)
    print(f'Adding connection between {val1} and {val2}')
    test.add_edge(val1,val2)
print(test.nodes)
test.show_connections()