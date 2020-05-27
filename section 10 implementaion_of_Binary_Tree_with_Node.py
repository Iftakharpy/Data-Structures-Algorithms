class Node:
    def __init__(self,value):
        self.value = value
        self.high = None
        self.low = None
    def __repr__(self):
        return f'[value:{self.value},\nhigh:{self.high},low:{self.low}]'


class Binary_Tree:
    def __init__(self,value=None):
        if value==None:
            self.root = None
            self.length=0
        else:
            self.root = Node(value)
            self.length=1

    def __repr__(self):
        return f"root:{self.root}\nlength:{self.length}"

    def insert(self,value):
        new_node = Node(value)
        if self.root==None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value<=current_node.value:
                if current_node.low==None:
                    current_node.low=new_node
                    self.length+=1
                    return
                current_node=current_node.low
            else:
                if current_node.high==None:
                    current_node.high=new_node
                    self.length+=1
                    return
                current_node=current_node.high

    def lookup(self,value):
        current_node = self.root
        while True:
            if value==current_node.value:
                return True
            if value>current_node.value:
                current_node=current_node.high
                continue
            current_node = current_node.low
            if current_node.value==value:
                return True
            if current_node.high == None and current_node.low==None:
                return False

a=Binary_Tree()
vals = [9,20,4,1,6,21,19]
for i in vals:
    a.insert(i)
print(a)
a.remove(1)
print(a)