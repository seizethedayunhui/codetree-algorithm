first, second = map(int, input().split())

num_list = list()
num_list.append(first)
num_list.append(second)

for i in range(10) :
    if i < 2 :
        print(num_list[i], end=" ")
    else :
        ans = num_list[i-1] + v
        num_list.append(ans)
        print(num_list[i], end=" ")