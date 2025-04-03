N, M = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0

for num in num_list :
    if num == M :
        cnt += 1

print(cnt)