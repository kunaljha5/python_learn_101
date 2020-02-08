# You are given a two lists A and B. Your task is to compute their cartesian product (AXB).
# A = [1, 2]
# B = [3, 4]
# https://www.hackerrank.com/challenges/itertools-product/problem
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]



# Input Format
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
# Both lists have no duplicate integer elements.

# Output Format
# Output the space separated tuples of the cartesian product.



## INPUT 

##  1 2
##  3 4

## OUTPUT 
##  (1, 3) (1, 4) (2, 3) (2, 4)
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

lista = input().split()
listb = input().split()
A= []
B = []
for element in lista:
    A.append(int(element))
for element in listb:
    B.append(int(element))
A.sort()
B.sort()
for ele in list(product(A,B)):
    print(ele, end=' ')
