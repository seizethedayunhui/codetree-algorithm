N = int(input())

num_list = list()
for _ in range(N) :
    num_list.append(int(input()))

num_sum = 0
for num in num_list :
    num_sum += num

num_str = str(num_sum)
num_str = num_str[1:] + num_str[0]
print(num_str)