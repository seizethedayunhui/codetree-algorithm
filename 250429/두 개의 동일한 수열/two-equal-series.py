n = int(input())

A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

A_arr.sort()
B_arr.sort()

flag = True

for i in range(n) :
    if A_arr[i] != B_arr[i] :
        flag = False
        break

if flag :
    print("Yes")
else :
    print("No")