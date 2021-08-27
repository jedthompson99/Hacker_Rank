# def doormat(height, width):
#     for i in range(width):
#         print(
#     # return

# pattern = ".|."

# height, width = map(int, input().split())

# for i in range((height // 2)):
#     top = (pattern*(2*i+1)).center(width, "-")

#     print(top)


height, width = map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(width, '-') for i in range(height//2)]
print('\n'.join(pattern + ['WELCOME'.center(width, '-')] + pattern[::-1]))
