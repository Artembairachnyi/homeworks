non_unick_list = ["John Dow", "John Dow", "Marta Dow", "Alex Dow", "Marshal Dow", "Marta Dow"]
unique_list = []
for x in non_unick_list:
    if x not in unique_list:
     unique_list.append(x)
for x in unique_list:
    print(x)
