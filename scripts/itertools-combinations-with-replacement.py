#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

if '__main__' == __name__:
    list0 = input().split()
    integer0= int(list0[1])
    string0= list0[0]
    string0 = ''.join(sorted(string0))
    data0 = list(combinations_with_replacement(string0,integer0))
    sorted_data0 = []
    for each in data0:
        item = ''.join(each)
        sorted_data0.append(item)
    sorted_data0.sort()
    for i in sorted_data0:
        print(i)

