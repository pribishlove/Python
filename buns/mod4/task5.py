file = open("test.txt")
s = file.readline()
my_dict = {}
for letter in s:
    if letter in my_dict:
        my_dict[letter] += 1
    else:
        my_dict[letter] = 1
sort_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=False))
with open('test.txt', 'w') as file:
    for key, value in sort_dict.items():
        file.write(f'{key}: {value}\n')