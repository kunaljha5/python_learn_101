# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given scores. Store them in a list and find the score of the runner-up. 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ### Convert map into a list
    arr_list = list(arr)
    ### convert list into revrese sorted list
    arr_list.sort(reverse=True)
    # define empty uniq list to remove 2 winners with same score. 
    uniq_list =[]
    # itterate over each element of the arr_list
    for each in arr_list:
        # check if that elemet exists in the uniq_list if not then add in the uniq_list
        if each not in uniq_list:
            uniq_list.append(each)
    print(uniq_list[1])

