#poject closed

list1=[x for x in range(1,11,2)]
list2=[x for x in range(0,11,2)]
sorted_list=[]
print(list1,list2)

list1_indx = 0
list2_indx = 0
#O(1)
def check_index_error(lst,indx):
    try:
        a=lst[indx]
        return False
    except IndexError:
        return True

#O(a+b) | a=len(list1),b=len(list2)
while (not check_index_error(list1,list1_indx)) or (not check_index_error(list2,list2_indx)):
    if check_index_error(list1,list1_indx):
        while not check_index_error(list2,list2_indx):
            sorted_list.append(list2[list2_indx])
            list2_indx+=1
        break
    if check_index_error(list2,list2_indx):
        while not check_index_error(list1,list1_indx):
            sorted_list.append(list1[list1_indx])
            list1_indx+=1
        break
    if list1[list1_indx]==list2[list2_indx]:
        sorted_list.append(list1[list1_indx])
        list1_indx+=1
        sorted_list.append(list2[list2_indx])
        list2_indx+=1
    if list1[list1_indx]<list2[list2_indx]:
        sorted_list.append(list1[list1_indx])
        list1_indx+=1
    sorted_list.append(list2[list2_indx])
    list2_indx+=1

print(sorted_list)