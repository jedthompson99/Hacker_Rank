def cube(n):
    return n**3


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


# generatorUsingYield(10)

# generatedValues = generatorUsingYield(10)
# print(generatedValues)

originalList = range(1, 11)
for x in originalList:
    print(x)

cubesUsingListComprehensions = [cube(x) for x in originalList]
print(cubesUsingListComprehensions)
