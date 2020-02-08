#Task
#You are given a S string.
#Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

#Input Format

#A single line containing the space separated string S and the integer value k.

#Constraints
0 < k <= len(S)

#The string contains only UPPERCASE characters.

#Output Format

#Print the permutations of the string S on separate lines.

#Sample Input

#HACK 2

#Sample Output
# https://www.hackerrank.com/challenges/itertools-permutations/problem
#AC
#AH
#AK
#CA
#CH
#CK
#HA
#HC
#HK
#KA
#KC
#KH

#Explanation

#All possible size
#permutations of the string "HACK" are printed in lexicographic sorted order.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    str_in = input().split()
    string0 = list(str_in[0])
    num0 = int(str_in[1])
    permutations_comb = list(permutations(string0,num0))
    lexSort =[]
    for each in permutations_comb:
        item = ''.join(each)
        lexSort.append(item)
    lexSort.sort()
    for i in lexSort:
        print(i)


