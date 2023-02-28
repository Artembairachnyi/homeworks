def square_params(argument):
    perimeter_func = argument * 4
    area_func = argument * argument
    square_func = argument * (2 ** 0.5)
    calculation_result = (perimeter_func, area_func, square_func)
    return calculation_result


if __name__ == '__main__':
    final_res = square_params(40)
print(final_res)
