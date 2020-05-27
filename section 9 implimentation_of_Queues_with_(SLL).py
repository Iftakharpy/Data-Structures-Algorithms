class Queues:
    def __init__(self,value=None):
        if value==None:
            self.queue = {'value':None,'next':None}
            self.tail = self.queue
            self.length = 0
        else:
            self.queue = {'value':value,'next':None}
            self.tail = self.queue
            self.length = 1
    
    def __repr__(self):
        return f'queue:{self.queue}\ntail:{self.tail}\nlength:{self.length}'
    
    def enqueue(self,value):
        if self.length<=0:
            self.__init__(value)
            return
        new_node = {'value':value,'next':None}
        self.tail['next'] = new_node
        self.tail = new_node
        self.length+=1

    def dequeue(self):
        if self.length<=0:
            return 0
        if self.length == 1:
            val = self.queue['value']
            self.__init__(None)
            return val
        val = self.queue['value']
        self.queue=self.queue['next']
        self.length-=1
        return val

    def peek(self):
        return self.queue['value']
    
    def get_list(self):
        lst = []
        if self.length==0:
            return lst
        temp = self.queue
        while temp['next']!=None:
            lst.append(temp['value'])
            temp=temp['next']
        lst.append(temp['value'])
        return lst
    
    def is_empty(self):
        return self.length <= 0

a = Queues()
lst = ['Joy','Matt','Pavel','Samir']
for i in lst:
    a.enqueue(i)
    print(a.get_list())

print(a.peek())

for i in range(4):
    print(a.dequeue())