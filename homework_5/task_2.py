import pickle

with open('tuple_list_1.txt ', 'r+b') as file:
    operands = file.read()
    operands_list = pickle.loads(operands)
    # print(operands_list)

summa = []
for operand in operands_list:
    if operand[2] == 1:
        summa.append(operand[0] + operand[1])
    elif operand[2] == 2:
        summa.append(operand[0] - operand[1])

    elif operand[2] == 3:
        summa.append(operand[0] * operand[1])

        print(summa)
