count=1
def call(a):
    print(a)
    a+=1
    call(a)

call(count)
#recurrsion depth may vary from machine to machine or may be programm to programm on the same device
