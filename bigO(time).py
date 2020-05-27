#Big O only cares about worst case.
#How many calculations and comparisons it takes to end a function when input grows is the time complexity of a function.


#O(n)
def big_O_n(array):
    for item in array:
        if item.lower()=='nemo':
            print('found NEMO')

#O(1)
def big_O_1(array):
    print(f'First item of the list is: {array[0]}')

#O(n^2)
def big_O_n_square(num):
    for base in range(num):
        for exponent in range(num):
            print(f'{base}^{exponent} = {base**exponent}')

#O(n^3)
def big_O_n_qube(num):
    count = 0
    for num1 in range(num):
        for num2 in range(num):
            for num3 in range(num):
                count+=1
                print(f'{num1}+{num2}+{num3} = {num1+num2+num3}')
    print(f'operated {count} times.')

#O(a+b)
def big_O_a_sum_b(a,b):
    for i in range(1,a+1):
        print(a*i)
    for i in range(1,b+1):
        print(b*i)

#O(a*b)
def big_O_a_times_b(arr1,arr2):
    for item_arr1 in arr1:
        for item_arr2 in arr2:
            if item_arr1==item_arr2:
                return True
    return False

print(big_O_a_times_b([1,2,4,6,8,'a'],['a']))