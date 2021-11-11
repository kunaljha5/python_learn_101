# using the inbuilt modules

def rev(s):
    return "-".join(s.split()[::-1])


s = "This is the best"
print(rev(s))