def print_func (*args):
    args_str = [str(arg) for arg in args]

if __name__ == '__main__':
    print_func('hello world')