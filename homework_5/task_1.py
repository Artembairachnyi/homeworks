import random

random_list = []
for _ in range(100):
    random_list.append(tuple(random.sample(range(1, 4), 3)))
    # print(type(random_list))

    import pickle
    ordered_list = pickle.dumps(random_list)


    with open('tuple_list_1.txt ', 'w+b') as file:
     file.write(ordered_list)
    # print(ordered_list)

    with open('tuple_list_1.txt ', 'r+b') as file:
        result = file.read()
        final_res = pickle.loads(result)
        # print(type(final_res))

