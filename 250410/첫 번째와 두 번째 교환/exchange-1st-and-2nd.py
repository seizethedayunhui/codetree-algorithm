string = input()
char1 = string[0]
char2 = string[1]

string_list = list(string)

for i in range(len(string_list)) :
    if string_list[i] == char1 :
        string_list[i] = char2
    elif string_list[i] == char2 :
        string_list[i] = char1

ans = "".join(string_list)
print(ans)