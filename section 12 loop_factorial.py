num = int(input('Enter a number to get the factorial of the number.\n'))
factorial = 1
while num>=1:
    factorial *= num
    num-=1

print(factorial)