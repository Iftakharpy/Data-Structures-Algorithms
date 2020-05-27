#O(a*b)
def contains_common(arr1,arr2):
    for item_arr1 in arr1:
        for item_arr2 in arr2:
            if item_arr1==item_arr2:
                return True
    return False

#O(a+b) time
#O(n) space
def contains_common(arr1,arr2):
    seen_items = {}
    for item in arr1:
        if not seen_items.get(item):
            seen_items[item]=True
    for item in arr2:
        if seen_items.get(item):
            return True
    return False