string = input()
elem_string = input()
string_len = len(string)
elem_len = len(elem_string)


for i in range(string_len - elem_len + 1) :
    flag = True
    for j in range(elem_len) :
        if string[i+j] != elem_string[j] :
            flag = False
            break
    if flag :
        print(i)
        break

if not flag :
    print(-1)
