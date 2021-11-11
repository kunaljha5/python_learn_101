# using no modules

def rev(s):

    length = len(s)
    spaces = [' ']
    words = []
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))


print(rev("This is the best"))
