A, B = map(int, input().split())

cnt_sum = 0
for i in range(A, B+1) :
    cnt_sum += i

print(cnt_sum)