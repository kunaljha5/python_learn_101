# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
# https://www.hackerrank.com/challenges/itertools-combinations/problem
if __name__ == '__main__':
    # Python | Way to read each item of a input line and make list of it.
    input_1 = input().split()
    string0 = input_1[0]
    #Python | Ways to sort letters of string alphabetically
    string0 = ''.join(sorted(string0))
    integer0 = int(input_1[1])
    for i in range(1,integer0+1):
        data0 = list(combinations(string0,i))
        sort_data = []
        for each in data0:
            item = ''.join(each)
            sort_data.append(item)
        sort_data.sort()
        for i  in sort_data:
            print(i)
        
