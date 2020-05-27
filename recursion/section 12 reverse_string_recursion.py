# my solution
def revrse_string(string):
    reversed = []
    if len(string)==1 or len(string)==0:
        return string
    def foo(x=len(string)-1):
        if x==0:
            reversed.append(string[x])
            return x
        reversed.append(string[x])
        return foo(x-1)
    foo()
    return "".join(reversed)


#stack overflow fails with empty string.
def revrse_string(string):
    if len(string)==1:
        return string
    return revrse_string(string[1:])+string[0]