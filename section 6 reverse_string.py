usr_input = input('Write something : ')
reversed_str = ''
#custom implementation
#O(n) time
#O(n) space
for i in range(len(usr_input)-1,-1,-1):
    reversed_str+=usr_input[i]
print(reversed_str)

#built in function
print(input('Write something : ')[::-1])
