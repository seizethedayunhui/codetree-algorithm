# PYTHON에서는 함수 위에 정의해주기만 하면 전역변수가 됨.

string1 = input()
string2 = input()

def find_start_index(string1, string2) :

    str_len1 = len(string1)
    str_len2 = len(string2)

    for i in range(str_len1 - str_len2 + 1) :
        find_flag = True
        for j in range(str_len2) :
            if string1[i+j] != string2[j] :
                find_flag = False
                break
       
        if find_flag :
            return i
    return -1

ans = find_start_index(string1, string2)

print(ans)