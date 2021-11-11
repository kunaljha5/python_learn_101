# using the inbuilt modules

def rev(s):
    s = s.split()
    s.reverse()
    return " $ ".join(s)


print(rev("This is the best"))
