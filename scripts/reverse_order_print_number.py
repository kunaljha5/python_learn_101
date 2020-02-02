

# https://www.hackerrank.com/challenges/python-print/problem?
# Without using any string methods, try to print the following 
# input 3
# print 123 
# input 5
# 12345

if __name__ == '__main__':
    n = int(input())
    array = []
    for i in range(n):
        i = i +1
        array.append(i)
    
    array.sort(reverse=False)
    for j in array:
        print(j, end = '')
    


