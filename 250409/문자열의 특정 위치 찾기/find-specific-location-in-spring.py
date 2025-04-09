string, char = input().split()

flag = -1

for i in range(len(string)) :
    if string[i] == char :
        print(i)
        flag = 1
        break

if flag < 0 :
    print("No")