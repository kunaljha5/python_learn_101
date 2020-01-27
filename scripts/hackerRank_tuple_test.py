# https://www.hackerrank.com/challenges/python-tuples/problem
# Given an integer, , and space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of
#
# .
#
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported. 
#
# Input Format
#
# The first line contains an integer,n , denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.
#
# Output Format
#
# Print the result of hash(t).

if __name__ == '__main__':
    # Read the first input line for value n
    n = int(input())
    # read the second line of stdin and save as map
    integer_list = map(int, input().split())
    # convert the map into a tuple
    integer_tuple =  tuple(integer_list)
    # print the hash of tuple
    print(hash(integer_tuple))
