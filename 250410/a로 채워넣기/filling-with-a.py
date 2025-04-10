string = input()
string_list = list(string)

string_list[1] = 'a'
string_list[-2] = 'a'

for elem in string_list:
    print(elem, end="")