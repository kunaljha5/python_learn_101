# https://www.hackerrank.com/challenges/compress-the-string/problem

# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

# You are given a string. Suppose a character '' occurs consecutively times in the string. Replace these consecutive occurrences of the character '' with in the string.
# For a better understanding of the problem, check the explanation.
# Input Format
# A single line of input consisting of the string.
#
# Output Format
#
# A single line of output consisting of the modified string.
# INPUT 1222311
# OUTPUT (1, 1) (3, 2) (1, 3) (2, 1)

# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import groupby

if '__main__' == __name__:
    stringlist0 = list(input())
    list0 = []
    #print(stringlist0)
    for key,grp in groupby(stringlist0):
        #print(key)
        #print(list(grp))
        length0 = len(list(grp))
        item = (length0,int(key))
        list0.append(item)
    #print(list0)
    for each in list0:
        print(each, end=' ')
