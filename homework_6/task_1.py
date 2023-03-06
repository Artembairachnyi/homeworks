def arifmetic_func(num_1: int, num_2: int, operator):
    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '/':
        result = num_1 / num_2
    elif operator == '*':
        result = num_1 * num_2
    else:
        print('Not known operation:', operator)
        return None
    return result


if __name__ == '__main__':
    result = arifmetic_func(10, 3, '1')
    print(result)
