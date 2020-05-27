class Stack:
    def __init__(self,value):
        self.stack = []
        self.stack.append(value)
    
    def __repr__(self):
        return f'stack:{self.stack}\nlength:{len((self.stack))}'
    
    def get_list(self):
        return self.stack
    
    def peek(self):
        return self.stack[-1]

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack)==0

a=Stack(0)

for i in range(1,11):
    a.push(i)

print(a.pop())