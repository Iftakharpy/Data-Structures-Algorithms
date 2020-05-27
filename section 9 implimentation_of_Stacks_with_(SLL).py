class Node:
    def __init__(self,value=None):
        if value!=None:
            self.stack = {'value':value,'last':None}
            self.last = self.stack
            self.length = 1
        else:
            self.stack = {'value':value,'last':None}
            self.last = self.stack
            self.length = 0

class Stack(Node):
    def __init__(self,value=None):
        super().__init__(value)
    
    def __repr__(self):
        return f'{self.stack}\n{self.last}\n{self.length}'
    
    def get_list(self):
        lst = []
        if self.length==0:
            return lst
        temp_stack = self.stack
        for i in range(self.length):
            lst.append(temp_stack['value'])
            temp_stack=temp_stack['last']
        return lst

    def peek(self):
        return self.stack['value']

    def push(self,value):
        '''Adds a value on the top of the stack.(Means: Adding item at index 0 on the list.)'''
        if self.length == 0:
            self.__init__(value)
            return
        self.stack = {'value':value,'last':self.stack}
        self.length+=1
    
    def pop(self):
        '''Removes a value form the top of the stack.(Means: Removing the index 0 from the list.)'''
        if self.length<=0:
            return None
        if self.length == 1:
            val = self.stack['value']
            self.__init__(None)
            return val
        val = self.stack['value']
        self.stack = self.stack['last']
        self.length-=1
        return val

    def is_empty(self):
        return self.length == 0