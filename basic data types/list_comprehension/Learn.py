# def cube(n):
#     return n**3


# def simplifiedGenerator(n):
#     generatedResults = []
#     currentN = 1
#     while currentN <= n:
#         generatedResults.append(cube(currentN))
#         currentN += 1
#     return generatedResults


# print(simplifiedGenerator(10))


# def generatorUsingYield(n):
#     currentN = 1
#     while currentN <= n:
#         yield cube(currentN)
#         currentN += 1
#     generatedValues = generatorUsingYield(10)
#     print(generatedValues)


x = int(input())
y = int(input())
z = int(input())
n = int(input())
res = list()

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if(not(i+j+k == n)):
                ans = list()
                ans.append(i)
                ans.append(j)
                ans.append(k)
                res.append(ans)
print(res)
