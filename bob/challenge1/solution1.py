# using sorted in built function

def anagram(s1, s2):
    # remove white spaces and convert all to lower case
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


print(anagram("dog", "d go"))

print(anagram("public relations", "crap built on lies"))

print(anagram("clint eastwood", "old west action"))

print(anagram("dad", "bad"))

print(anagram("listen", "silent"))
