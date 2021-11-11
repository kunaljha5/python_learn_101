# using basic build in modules of python

def anagram(s1, s2):
    # remove white spaces and convert all to lower case
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # check same number of character in the string
    if len(s1) != len(s2):
        return False

    # count frequency for each number
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # do reverse for string2
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram("dog", "d go"))

print(anagram("public relations", "crap built on lies"))

print(anagram("clint eastwood", "old west action"))

print(anagram("dad", "bad"))

print(anagram("listen", "silent"))
