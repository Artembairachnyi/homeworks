users_id = [75, 83, 82, 14, 21, 22, 51, 12, 28]


def sort_func(number):
    if number % 2 == 0:
        return True


def filter_func(func, sequense):
    return [i for i in sequense if func(i)]


if __name__ == '__main__':
    filtered_id = filter_func(sort_func, users_id)
    print(filtered_id)
