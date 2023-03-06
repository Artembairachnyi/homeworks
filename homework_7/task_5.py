def all_func(argument):
    for i in argument:
        if not i:
            return 'False'
    else:
        return 'True'


if __name__ == '__main__':
    report = ['Igor', 123, ]
    my_all = all_func(report)
    print(my_all)
