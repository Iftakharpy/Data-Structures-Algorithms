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

    #O(1)
    # def get_length(self):
    #     return self.length
    # #O(n)
    # def get_list(self):
    #     lst = []
    #     temp_data = self.head
    #     for i in range(self.length):
    #         lst.append(temp_data['value'])
    #         if temp_data['next']==None:
    #             break
    #         temp_data=temp_data['next']
    #     return lst
    #O(1)
    #O(1)
    def prepend(self,value):
        if self.length==0:
            self.head = self._make_node(value)
            self.tail = self.head
            self.length+=1
            return None
        mk_first_node = self._make_node(value)
        mk_first_node['next'] = self.head
        self.head = mk_first_node
        self.length+=1
    #O(1)
    def insert(self,index=None,value=None):
        if index==None:
            raise IndexError("You haven't specified index")
        if index<=0:
            self.prepend(value)
            return None
        if index>=self.length:
            self.append(value)
            return None
        pointer = self._navigate_to_pointer(index)
        new_node = self._make_node(value)
        new_node['next'] = pointer['next']
        pointer['next'] = new_node
        self.length+=1
    #O(1)
    def remove_first(self):
        if self.length==1:
            val = self.head['value']
            self.head = {'value':None,'next':None}
            self.tail = self.head
            self.length = 0
            return val
        val = self.head['value']
        head = self.head['next']
        self.head = head
        self.length-=1
        return val
    #O(1)
    def remove_last(self):
        if self.length==1:
            return self.remove_first()
        pointer = self._navigate_to_pointer(self.length-1)
        val = pointer['value']
        pointer['next'] = None
        self.tail = pointer
        self.length-=1
        return val
    #O(n)
    def remove_index(self,index=None):
        if index==None:
            raise IndexError("You didn't specified index")
        if index>=self.length-1:
            self.remove_last()
            return None
        if index<=0:
            self.remove_first()
            return None
        #saving the index before the target index
        pointer_before_target = self._navigate_to_pointer(index)
        val = pointer_before_target['next']['value']
        #saving the index after the target index
        pointer_after_target = pointer_before_target['next']['next']
        pointer_before_target['next'] = pointer_after_target
        self.length-=1
        #returning the vale of removed index
        return val
    #O(n)
    def remove_value(self,value):
        pointer = self.head
        if pointer['value']==value:
            self.remove_first()
            return
        while pointer['next']!=None:
            previous_pointer = pointer
            pointer = pointer['next']
            if pointer['value']==value:
                if pointer==self.tail:
                    self.remove_last()
                    break
                next_pointer = pointer['next']
                previous_pointer['next']=next_pointer
                self.length-=1
                break
        else:
            raise ValueError(f'Value:"{value}" is not present in the linked list')
    
    #O(n)
    def reverse(self):
        if self.length == 0:
            raise ValueError("You can't inverse an empty list")
        if self.length == 1:
            return
        reversed_ll = Doubly_Linked_List()
        origin_ll = self.head 
        while origin_ll['next']!=None:
            reversed_ll.prepend(origin_ll['value'])
            origin_ll=origin_ll['next']
        reversed_ll.prepend(origin_ll['value'])
        self.head = reversed_ll.head
        self.tail = reversed_ll.tail

a=Doubly_Linked_List()
for i in range(2):
    a.append(i)
print(a)
print(a.tail)
print(a.head)