def fibonacci_nth_term(index,memory={}):
    if index in memory:
        return memory[index]
    if index<2:
        memory[index]=index
        return memory[index]
    memory[index] = fibonacci_nth_term(index-1,memory)+fibonacci_nth_term(index-2,memory)
    return memory[index]


print(fibonacci_nth_term(int(input('Enter a possitive number\n'))))