with open('text.txt', 'r') as file:
    the_text = file.read()

test_str = the_text
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(all_freq)


