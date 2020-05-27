# Big O only cares about worst case.
# Everything is simillar to the big O of time. 
# But here how much memory is used when input scales is counted to determine the space complexity.

#O(1) space
#O(n) time
def print_all_the_items(array):
    for i in array:
        print(i)


#O(n) space
#O(n) time
def squire_items(array):
    squired = []
    for i in array:
        squired.append(i**2)
    print(squired)
    return squired

squire_items([x for x in range(1001)])