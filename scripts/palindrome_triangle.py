# https://www.hackerrank.com/challenges/triangle-quest-2/problem
#  palindromic triangle 
# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1): 
    print(pow(((pow(10,i)-1)//9),2))
