def max_func(*args):
    max_item = args[0]
    for i in args:
        if i > max_item:
            max_item = i

    return max_item


def min_func(*args):
    min_item = args[0]
    for i in args:
        if i < min_item:
            min_item = i

    return min_item


if __name__ == '__main__':
    numb = [2, 34, 6, 4, 3, 8, 1, 7, 5, 26, 34, 76]
    check = max_func(*numb)
    print(check)
minimum = min_func(*numb)
print(minimum)
