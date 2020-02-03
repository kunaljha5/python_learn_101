# https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Sample input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample output 
# 56.00


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        # print(name)
        # print(line)
        # print(map(float, line))
        scores = list(map(float, line))
        # print(scores)
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        a  = 0.0
        c = 0.0
        for each in student_marks[query_name]:
            a = a + each
            c = c + 1.0
        # print(a/c)
        print("%.2f" % round(a/c,2))



