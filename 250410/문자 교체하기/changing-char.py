string1, string2 = input().split()

string1_list = list(string1)
string2_list = list(string2)

for i in range(2) :
    string2_list[i] = string1_list[i]

ans = ''.join(string2_list)
print(ans)
