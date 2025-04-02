num_list = list(map(int, input().split()))

for i in range(len(num_list)) :
    if not num_list[i] :
        ans = num_list[i-1] + num_list[i-2] + num_list[i-3]
        break

print(ans)