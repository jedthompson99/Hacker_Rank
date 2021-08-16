if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

    # example 1 podily16

    N = int(input())
    stud_dict = dict()

    for i in range(N):
        tmp = input().split()
        name = tmp[0]
        stud_dict[name] = (float(tmp[1]), float(tmp[2]), float(tmp[3]))

    name = input()
    print('%.2f' % (sum(stud_dict[name]) / 3.0))

    # example 2

    # n = int(input())
    # student_marks = {}

    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

    # print("{0:.2f}".format(
    #     round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))

    # Example 3

# N = int(input())
# final = list()
# for i in range(N):
#     lst = list()
#     name = str(input())
#     marks = float(input())
#     lst.append(name)
#     lst.append(marks)
#     final.append(lst)
# k = list()
# for i in range(len(final)):
#   k.append(final[i][1])
# x = min(k)
# k1 = list()
# for i in range(len(k)):
#   if x != k[i]:
#     k1.append(k[i])
# y = min(k1)
# student = list()
# for i in range(len(final)):
#   if y == final[i][1]:
#     student.append(final[i][0])
# student.sort()
# for i in range(len(student)):
#   print(student[i])
