# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/python-mod-divmod/problem
# Sample Input
# 177
# 10
# Sample Output
# 17
# 7
# (17, 7)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    answer  = divmod(x,y)
    print(x//y)
    print(x%y)
    print(answer)
