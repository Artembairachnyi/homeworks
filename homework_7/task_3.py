def pizza_square(radius: int) -> float:
    return 3.14 * radius ** 2


def profit_order(callbeck, sequence: list):
    profits = []
    for r in sequence:
        if callbeck(r):
            profits.append(callbeck(r))
    return profits


if __name__ == '__main__':
    pizza_radius = [15, 22, 25]
    res = profit_order(pizza_square, pizza_radius)
    print(res)
