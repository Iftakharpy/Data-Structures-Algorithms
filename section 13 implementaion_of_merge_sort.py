#O(1)
def check_index_error(lst,indx):
    if indx>=0 and indx<len(lst):
        return False
    return True

#time O(left+right) | space O(left+right)
def merge(left, right):
    sorted_arr = []
    # print('merging :',left,'and',right)
    if not left and not right:
        return sorted_arr
    if not left or not right:
        if left:
            return left
        return right
    max_left = len(left)-1
    min_left = 0
    max_right = len(right)-1
    min_right=0
    while min_left<=max_left and min_right<=max_right:
        if check_index_error(left,min_left) or check_index_error(right,min_right):
            break
        if left[min_left]<=right[min_right]:
            sorted_arr.append(left[min_left])
            min_left+=1
            continue
        if left[min_left]>=right[min_right]:
            sorted_arr.append(right[min_right])
            min_right+=1
    if min_right>max_right:
        while min_left<=max_left:
            sorted_arr.append(left[min_left])
            min_left+=1
    if min_left>max_left:
        while min_right<=max_right:
            sorted_arr.append(right[min_right])
            min_right+=1
    return sorted_arr

#time O(Nlog(N)) space(n)
def merge_sort(array):
    if len(array)<=1:
        return array

    # Split Array in into right and left
    mid_index = len(array)//2
    left = array[:mid_index]
    right = array[mid_index:]

    #recursively calling the function until the array is divided into smallest peaces(single items)
    #and passing the peacies to merge function to merge the small arrays
    return merge(merge_sort(left),merge_sort(right))







#test
#test
from random import randint
arr = []
for i in range(999999):
    arr.append(randint(0,100))
# print(arr)
print(merge_sort(arr))