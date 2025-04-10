string = input()
string_list = list(string)

for _ in range(len(string_list)-1) :
    index = int(input())
    if index > len(string_list) :
        removed = string_list.pop(-1)
    else :
        removed = string_list.pop(index)
    print("".join(string_list))