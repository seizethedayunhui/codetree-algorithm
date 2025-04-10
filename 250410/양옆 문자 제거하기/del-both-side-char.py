string = input()

string_list = list()

for i in range(len(string)) :
    if i != 1 and i != len(string)-2 :
        string_list.append(string[i])

print("".join(string_list))
