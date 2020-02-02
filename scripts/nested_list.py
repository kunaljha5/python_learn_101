
# https://www.hackerrank.com/challenges/nested-list/problem
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Output 
# Berry
# Harry
if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([])
        arr[_]= [name, score]
    smarks =  []

    for i in range(len(arr)):
        marko = arr[i][1]
        smarks.append(marko)

    smarks.sort(reverse=False)
    new_list = []

    for k in smarks:
        if k not in new_list:
            new_list.append(k)

    second_lowest = new_list[1]
    names_list = []

    for each in range(len(arr)):
        if second_lowest in arr[each]:
            name = arr[each][0]
            names_list.append(name)
    
    names_list.sort()
    for each in names_list:
        print(each)




