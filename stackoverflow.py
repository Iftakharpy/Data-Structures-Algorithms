class Doubly_Linked_List:
    #O(1)
    def __init__(self,value=None):
        if value==None:
            self.head = {'value':None,'prev':None,'next':None}
            self.tail = None
            self.length = 0
        else:
            self.head = {'value':value,'prev':None,'next':None}
            self.tail = self.head
            self.length = 1
    #O(1)
    def __repr__(self):
        return f'head:{self.head}\ntail:{self.tail}\nlength:{self.length}'
    def _navigate_to_pointer(self,index):
        pointer_before_insertion = self.head
        for i in range(index-1):
            pointer_before_insertion = pointer_before_insertion['next']
        return pointer_before_insertion
    #O(1)
    def _make_node(self,value):
        return {'value':value,'prev':None,'next':None}
    def append(self,value):
        if self.length==0:
            self.head = self._make_node(value)
            self.tail = self.head
            self.length+=1
            return None
        new_last_node = self._make_node(value)
        new_last_node['prev'] = self.tail
        self.tail['next'] = new_last_node
        self.tail = new_last_node
        self.length+=1
    def iterate(self,value='next'):
        if value=='next':
            pointer = self.head
            while pointer:
                yield pointer["value"]
                pointer = pointer["next"]
        else:
            pointer = self.tail
            while pointer:
                yield pointer["value"]
                pointer = pointer["prev"]

dlist = Doubly_Linked_List()
dlist.append(1)
dlist.append(2)
dlist.append(3)
print(dlist)

for item in dlist.iterate():
    print(item)