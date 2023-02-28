def is_prime(arg: int):
    if arg >= 2 and arg <= 100:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    result = is_prime
    result(100)
