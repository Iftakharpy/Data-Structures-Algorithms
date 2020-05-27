#space O(1) 
#time O(n^2) 
# worst case: Sorted in descending order  | O(n^2)
# best case: Nearly sorted  | O(n)
def insertion_sort(array,reversed=False):
    length = len(array)

    #looping from 1-st index to the last index
    for i in range(1,length):
        #saving the value of i-th index
        shifting_value = array[i]

        #saving (i-1)th index to move(value at index i-1) or compare
        carring_index = i-1
        if not reversed:
            #sorting in ascending order
            #looping until carring_index's value gets into the correct place
            while carring_index>=0 and shifting_value<array[carring_index]:

                #swaping the i-th index's value with i-1(until it gets into the correct place)
                array[carring_index+1] = array[carring_index]
                #decrasing the carring_index to move the value one more time with previous index
                carring_index-=1

            #if value is already in the correct place then save the value right here or else save the value into the modefied index by while loop
            array[carring_index+1] = shifting_value
        else:
            #sorting in descending order
            #looping until carring_index's value gets into the correct place
            while carring_index>=0 and shifting_value>array[carring_index]:
 
                #swaping the i-th index's value with i-1(until it gets into the correct place)
                array[carring_index+1] = array[carring_index]
                #decrasing the carring_index to move the value one more time with previous index
                carring_index-=1

            #if value is already in the correct place then save the value right here or else save the value into the modefied index by while loop
            array[carring_index+1] = shifting_value
    return array


#test
from random import randint
arr = []
for i in range(5):
    arr.append(randint(0,10))
print(arr)
print(insertion_sort(arr))