
# Boiler Plate
# n = int(input())
# arr = map(int, input().split())

# My thoughts
# def runner_up(arr, ):
# answer = map(runner_up, arr)
# print(arr)

# n = int(input())
# n = sorted(n)

# print(n[-2])

# Example 1
n = int(input())
a = map(int, input().split(" "))
a = list(a)
mx1 = a[0]
mn = a[0]
for i in a:
    if(i > mx1):
        mx1 = i
    if(i < mn):
        mn = i
mx2 = mn
for i in a:
    if(i > mx2 and i < mx1):
        mx2 = i
print(mx2)


# Example 2
# # n = input()
# a = map(int, input().split())
# a = list(set(a))
# a.remove(max(a))
# print(max(a))


# Example 3
n = int(input())
a = map(int, input().strip().split())
a = list(a)
mx1 = a[0]
mn = a[0]
for i in a:
    if(i > mx1):
        mx1 = i
    if(i < mn):
        mn = i
mx2 = mn
for i in a:
    if(i > mx2 and i < mx1):
        mx2 = i
print(mx2)

# Example 4
# n = int(input())
# numb = input()
# lis = list(map(int, numb.split()))
# big, sbig = -6000, -6000
# for i in lis:
#     if (i > big):
#         big, sbig = i, big
#     elif (i < big and i > sbig):
#         sbig = i
# print (sbig)
