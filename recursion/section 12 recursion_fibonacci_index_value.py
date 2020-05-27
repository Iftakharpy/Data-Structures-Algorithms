# series: 0,1,1,2,3,5,8,13,21,34,55,89,144

#if index is too large it will raise recurssion error.
#And this recursive programm gets annoyingly slow(slows down expontialy| and also spaces complexity grows exponentially)
def index_value_fibonacci_recursive(index): # time O(2^N) | space O(2^N)
    if index<2:
        return index
    return index_value_fibonacci_recursive(index-2)+index_value_fibonacci_recursive(index-1)

for i in range(1000):
    print(index_value_fibonacci_recursive(i))

#this is the most stable and fastest solution to the problem
def index_value_fibonacci_iterative(index): #time O(n) | space O(1)
    num1 = 0
    num2 = 1
    for i in range(index):
        num1,num2 = num2, num2+num1
    return num1


#can't calculate too large number
#after index=70 this formula produces larger value than the actual value. And this diffrence grows pretty quickly(almost exponentially)
from math import sqrt
def index_value_fibonacci_formula(index): #time O(1) | space O(1)
    #possitive value of phi
    pos_Phi = (1+sqrt(5))/2
    #negetive value of phi
    neg_Phi = (1-sqrt(5))/2

    #formula for the nth number of fibonacci
    nth_fibonachi = ((pos_Phi**index)-(neg_Phi**index))/sqrt(5)
    return round(nth_fibonachi)