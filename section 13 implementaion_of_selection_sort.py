def selection_sort(array,reversed=False):
    """if reversed flag is set to truthy value then it will return the array in reversed order."""
    length = len(array)
    index_of_min_value = 0
    min_index = 0
    max_index = length-1
    while min_index<max_index: #time O(n^2) | space O(1)
        # print(array)
        for i in range(min_index,length-1):
            if not reversed:
                if array[index_of_min_value]>array[i+1]:
                    index_of_min_value=i+1
                continue
            if array[index_of_min_value]<array[i+1]:
                    index_of_min_value=i+1
        array[min_index], array[index_of_min_value] = array[index_of_min_value], array[min_index]
        min_index+=1
        index_of_min_value=min_index
    return array

#test
from random import randint
arr = []
for i in range(9999):
    arr.append(randint(0,100))
# print(arr)
print(selection_sort(arr,True))