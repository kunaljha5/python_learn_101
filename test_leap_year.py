#https://www.hackerrank.com/challenges/write-a-function/problem

# Leap year verification. 

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year not in (1800, 1900, 2100, 2200, 2300,2500):
        leap = True    
    return leap

year = int(input())
