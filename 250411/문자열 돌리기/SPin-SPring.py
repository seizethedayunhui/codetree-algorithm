string = input()
string_len = len(string)

print(string)
for i in range(string_len) :
    new_string = string[string_len - (i+1):] + string[:string_len - (i+1)]
    print(new_string)
