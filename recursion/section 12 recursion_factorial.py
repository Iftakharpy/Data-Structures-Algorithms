num = int(input('Enter an integer number greather than 1 to get the factorial.\n'))

def factorial(number):
    #breaking condition
    if number==1:
        return 1
    # multipling number with all the numbers smaller than the number until number is 1.
    return number*factorial(number-1)

print(factorial(num))