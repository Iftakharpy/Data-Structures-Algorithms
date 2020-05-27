class Binary_Tree:
    def __init__(self,value=None):
        self.root = None
        self.length = 0
        if value:
            self.root=self._make_node(value)
            self.length=1
    def __repr__(self):
        return f'root:{self.root}\nlength:{self.length}'

    def _make_node(self,value):
        return {'value':value,'high':None,'low':None}
    

    def insert(self,value):
        new_node = self._make_node(value)
        if self.length==0:
            self.__init__(value)
            return
        temp=self.root
        while True:
            if value>=temp['value']:
                if temp['high']==None:
                    temp['high']=new_node
                    self.length+=1
                    return
                temp=temp['high']
                continue
            if temp['low']==None:
                temp['low']=new_node
                self.length+=1
                return
            temp=temp['low']
    def lookup(self,value):
        if self.length==0:
            return None
        temp=self.root
        while True:
            if temp['value']==value:
                return True
            if value>temp['value']:
                temp=temp['high']
                continue
            temp=temp['low']
            if temp['value']==value:
                return True
            if temp['high']==None and temp['low']==None:
                return False


#      9
#    /   \
#   4     20
#  /  \   /  \
# 1    6  15  200

test = Binary_Tree(9)
test.insert(4)
test.insert(6)
test.insert(1)
test.insert(20)
test.insert(15)
test.insert(200)


print(test)