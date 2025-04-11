num1, num2 = map(int, input().split())

num_sum = num1 + num2

num_sum = str(num_sum)

cnt = 0
for i in num_sum :
    if i == '1' :
        cnt += 1
print(cnt)