def largest_sum (arr):
    if len (arr) == 0:
        return print('Too Small')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


print(largest_sum([7,1,2,3,4,5,6,10, -12, 3, 21, -19]))