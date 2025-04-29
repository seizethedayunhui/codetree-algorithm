string = input()

string_list = list(string)
string_list.sort()

string = ''.join(string_list)

print(string)