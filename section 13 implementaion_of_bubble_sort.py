def is_sorted(array,reversed): #time O(n) | space O(1)
    length = len(array)
    for i in range(length-1):
        if not reversed:
            if not array[i]<=array[i+1]:
                return False
            continue
        if not array[i]>=array[i+1]:
                return False
    return True

def bubble_sort(array,reversed=False): #time O(n^2) | space O(1)
    """Takes an array in the array param and returns sorted by ascending order.\n Array can be sorted in reversed order by setting the reversed param to True.\n\nNote:Only numbers can be sorted with this function."""
    n = len(array)
    for i in range(n-1,0,-1):
        for j in range(i):
            # print(array)
            # print(j,i)
            if not reversed:
                if array[j] >= array[j+1]:
                    array[j], array[j+ 1] = array[j+1], array[j]
                    continue
                continue
            if array[j] <= array[j+1]:
                    array[j], array[j+ 1] = array[j+1], array[j]
                    continue
        #checking if the array is sorted or not
        if is_sorted(array,reversed):
            print('array is sorted')
            return array



#test
from random import randint
arr = []
for i in range(100):
    arr.append(randint(0,10))
print(bubble_sort(arr))