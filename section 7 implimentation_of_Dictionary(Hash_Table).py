import random

class Custom_Dictionary:
    #O(1)
    def __init__(self,size):
        if size ==0:
            raise ValueError("You can't have an array of size 0")
        self.size = size
        self.data = [[] for x in range(size)]
    #O(1)
    def __repr__(self):
        return str(self.data)

    #O(n)
    def _hash(self,key):
        hash=0
        for i in key:
            hash+=ord(i)
        index_of_data = (hash%self.size)-1
        return index_of_data
    
    #O(n)
    def get(self,key):
        index = self._hash(key)
        length = len(self.data[index])
        if self.data[index] and length>1:
            for i in range(length):
                if self.data[index][i][0]==key:
                    return self.data[index][i][1]          
        return self.data[index][0][1]

    #O(n)
    def assign(self,key,val):
        index = self._hash(key)
        length = len(self.data[index])
        key_exist = False
        if self.data[index] and length>1:
            for i in range(length):
                if self.data[index][i][0]==key:
                    key_exist=True
                    self.data[index][i]=[key,val]
                    break
        if not key_exist:
            self.data[index].append([key,val])
    
    #O(n)
    def get_keys(self):
        key = []
        for i in range(self.size):
            if self.data[i]:
                length = len(self.data[i])
                if length>1:
                    for j in range(length):
                        key.append(self.data[i][j][0])
                else:
                    key.append(self.data[i][0])
        return key
    #O(n)
    def get_values(self):
        val = []
        for i in range(self.size):
            if self.data[i]:
                length = len(self.data[i])
                if length>1:
                    for j in range(length):
                        val.append(self.data[i][j][1])
                else:
                    val.append(self.data[i][1])
        return val

#generators to test Custom_Dictionary
class generator:
    #generating keys for test
    def generate_keys(number_of_keys=10,length_of_keys=3):
        random_keys = []
        for i in range(number_of_keys):
            chrs =''.join([chr(random.randint(97,122)) for x in range(length_of_keys)])
            random_keys.append(chrs)
        return random_keys
    #generating values for test
    def generate_values(number_of_values=10,min_val=0,max_val=100):
        vals = []
        for i in range(number_of_values):
            val = random.randint(min_val,max_val)
            vals.append(val)
        return vals



records = 99999

#generating random keys and values to test Custom_Dictionary
keys = generator.generate_keys(records,5)
vals = generator.generate_values(records,0,1000)

real_dict = {}
#initializing Custom Dictionary
my_dict = Custom_Dictionary(20)

with open('my_dict_entry.txt','w') as f,open('real_dict_entry.txt','w') as f1:
    for (key,val) in zip(keys,vals):
        # print('asinging',key,'=',val)
        my_dict.assign(key,val)
        real_dict[key] = val
        f.write(f'{key} {val}\n')
        f1.write(f'{key} {val}\n')

with open('retrived_records_from_my_dict.txt','w') as f,open('retrived_records_from_real_dict.txt','w') as f1:
    for key in keys:
        val = my_dict.get(key)
        f.write(f'{key} {val}\n')
        f1.write(f'{key} {val}\n')

print('4 text files were written.')