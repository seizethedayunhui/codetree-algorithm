num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if not num_list[i] :
        num_list = num_list[:i]
        break

for j in range(len(num_list)-1, -1, -1) :
    print(num_list[j], end=" ")