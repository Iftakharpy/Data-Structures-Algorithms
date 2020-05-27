class Custom_List:
    #O(1)
    def __init__(self):
        self.length = 0
        self.data  =  []
    #O(1)
    def __repr__(self):
        return f'{self.length}\t{self.data}'
    #O(1)
    def length(self):
        return self.length
    
    #O(1)
    def add_as_last(self,val):
        self.data.append(val)
        self.length+=1
    
    #O(1)
    def del_last(self):
        self.length-=1
        return self.data.pop()
    
    #O(n)
    def add_as_first(self,val):
        self.data.insert(0,val)
        self.length+=1
    
    #O(n)
    def del_first(self):
        self.length-=1
        return self.data.pop(0)

test_arr = Custom_List()
# print(test_arr)
for i in range(40):
    test_arr.add_as_first(i)
    print(test_arr)
for i in range(test_arr.length):
    test_arr.del_first()
    print(test_arr)