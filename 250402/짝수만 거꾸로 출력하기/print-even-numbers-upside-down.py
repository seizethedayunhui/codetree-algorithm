N = int(input())

num_list = list(map(int, input().split()))

for i in range(len(num_list)-1, -1, -1) :
    if num_list[i] % 2 == 0:
        print(num_list[i], end=" ")