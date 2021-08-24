def swap_case(s):
    output = ''
    for x in s:
        if x.isupper() == True:
            output += (x.lower())
        elif x.isupper() != True:
            output += (x.upper())
        else:
            output += x
    return output


if __name__ == '__main__':
    s = str(input())
    result = swap_case(s)
    print(result)
