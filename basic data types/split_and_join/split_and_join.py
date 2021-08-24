def split_and_join(line):
    split_result = line.split()
    join_result = "-" .join(split_result)
    return join_result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
