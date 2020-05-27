#O(n^2) time
#O(1) space
def first_recurring_item(arr): #less storage more time
    print(arr)
    for i in range(len(arr)):
        for j in arr[:i]:
            print(f'comparing {arr[i]} and {j}')
            if j==arr[i]:
                return arr[i]
    return None


arr1 = [1,2,2,1,5,6,2,1,4]
arr2 = [2,4,1,5,3,5,1,2,4]
arr3 = [x for x in range(10)]
arr3.append(9)
'''
print(first_recurring_item(arr1))
print(first_recurring_item(arr2))
print(first_recurring_item(arr3))
'''


#O(n) time
#O(n) space
def first_recurring_item(arr): #less time more storage
    #hash table to keep track of seen elements
    seen_items = {}
    print(arr)
    for item in arr:
        print(f'checking {item}')
        if seen_items.get(item):
            return item
        seen_items[item]=True
    return None

'''
print(first_recurring_item(arr1))
print(first_recurring_item(arr2))
print(first_recurring_item(arr3))
'''