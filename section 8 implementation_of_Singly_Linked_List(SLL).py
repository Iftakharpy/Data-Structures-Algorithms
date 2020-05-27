class Singly_Linked_List:
    #O(1)
    def __init__(self,value=None):
        if value==None:
            self.head = {'value':None,'next':None}
            self.tail = None
            self.length = 0
        else:
            self.head = {'value':value,'next':None}
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
        return {'value':value,'next':None}
    #O(1)
    def get_length(self):
        return self.length
    #O(n)
    def get_list(self):
        lst = []
        temp_data = self.head
        for i in range(self.length):
            lst.append(temp_data['value'])
            if temp_data['next']==None:
                break
            temp_data=temp_data['next']
        return lst
    #O(1)
    def append(self,value):
        if self.length==0:
            self.head = self._make_node(value)
            self.tail = self.head
            self.length+=1
            return None
        new_last_node = self._make_node(value)
        self.tail['next'] = new_last_node
        self.tail = new_last_node
        self.length+=1
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
    #O(n)
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


#test
import random
a=Singly_Linked_List()

inserted_lst = []
commands = ['insert','append','remove_index','prepend','remove_value']
for i in range(99999):
    command = random.choice(commands)
    ll = a.get_list()
    # print(f'sll:{ll}\nsyl:{inserted_lst}')
    print(f'{ll==inserted_lst}\t|\t{len(inserted_lst)}\t|\t{i}\t|\t{command}')
    # print(f'{a.tail}')
    if len(ll) != len(inserted_lst):
        print(f'len(sll) : {len(ll)}')
        print(f'len(syl) : {len(inserted_lst)}')
        print(a)
        break
    if set(inserted_lst)!=set(ll):
        print(f'loop ran {i+1}. sets are not equal')
        break
    if len(inserted_lst)==0 and (command == 'remove_value' or command == 'remove_index'):
        print('skipping lst len is 0')
        continue
    if command == 'insert':
        val = random.randint(1,100)
        if len(inserted_lst)>1:
            indx = random.randint(0,a.get_length()-1)
        else:
            indx = 0
        # print(f'inserting {val} at index:{indx}')
        a.insert(indx,val)
        inserted_lst.insert(indx,val)
        continue
    elif command == 'prepend':
        val = random.randint(1,100)
        a.prepend(val)
        inserted_lst.insert(0,val)
        continue
    elif command == 'append':
        val = random.randint(1,100)
        a.append(val)
        inserted_lst.append(val)
        continue
    elif command == 'remove_value':
        # print(f'removing {val}')
        val = random.choice(inserted_lst)
        a.remove_value(val)
        inserted_lst.remove(val)
        continue
    indx = random.randint(0,len(inserted_lst)-1)
    a.remove_index(indx)
    inserted_lst.pop(indx)

print(f'sys--> len:{len(inserted_lst)} | lst:{inserted_lst}')
print(f'sll--> len:{a.get_length()} | sll:{a.get_list()}')
print(a.get_list()==inserted_lst)
