my_list = ['Ivan', 'Maria', 'Jane', 'Olaf', 'Margo', 'Nat']
odd_list = []
even_list = []

for x in my_list:
    if x % 2 == 0:
        odd_list.append(x)
    else:
        even_list.append(x)
    print(odd_list)
    print(even_list)
