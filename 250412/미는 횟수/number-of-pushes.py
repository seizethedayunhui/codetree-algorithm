A = input()
B = input()

cnt = 0
flag = False

for _ in range(len(B)) :
    if A == B :
        flag = True
        break
    else :
        A = A[-1] + A[0:-1]
        cnt += 1

if flag :
    print(cnt)
else :
    print(-1)
