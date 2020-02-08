# https://www.hackerrank.com/challenges/python-lists/problem

#Consider a list (list = []). You can perform the following commands:
#    insert i e: Insert integer at position.
#    print: Print the list.
#    remove e: Delete the first occurrence of integer.
#    append e: Insert integer    at the end of the list.
#    sort: Sort the list.
#    pop: Pop the last element from the list.
#    reverse: Reverse the list.
#
#Initialize your list and read in the value of
#followed by lines of commands where each command will be of the type
# INPUT 
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# prints listed above. Iterate through each command in order and perform the corresponding operation on your list.
# OUTPUT 
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
if __name__ == '__main__':
    N = int(input())
    klist = []
    for _ in range(N):
        action =input().split()
        # print(action)
        if action[0] == "insert":
            klist.insert(int(action[1]), int(action[2]))
        elif action[0] == "print":
            print(klist)
        elif action[0] == 'remove':
            klist.remove(int(action[1]))
        elif action[0] == 'append':
            klist.append(int(action[1]))
        elif action[0] == 'sort':
            klist.sort()
        elif action[0] == 'pop':
            klist.pop(-1)
            #print(klist)
        elif action[0] == 'reverse':
            klist.reverse()
            #print(klist)
        else:
            print("NA")


