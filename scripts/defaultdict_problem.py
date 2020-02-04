# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

d = defaultdict(list)

list1=[]

# read line and store the inputs seprated by space into seprate variables. 
n, m = map(int,input().split())

# run for loop for n iterations and read all the inputs and append them in d[a] d[b] list/array.
for i in range(0,n):
    d[input()].append(i+1) 

# run for loop for m iterations and read all possible values to examine.
for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i]) ))
    else:
        print(-1)
        
