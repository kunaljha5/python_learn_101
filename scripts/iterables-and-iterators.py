# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

_,s,n = input(),input().split(),int(input())
t = list(combinations(s,n))
# print(t)
f = [i for i in t if 'a' in i]
# print(f)
print(len(f)/len(t))
