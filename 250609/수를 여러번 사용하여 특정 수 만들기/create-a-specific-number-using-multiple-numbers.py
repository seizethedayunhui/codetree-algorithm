A, B, C = map(int, input().split())

max_sum = float('-inf')

# A를 더하는 횟수
for i in range(1001) :
    # B를 더하는 횟수
    for j in range(1001) :

        current_sum = (A * i) + (B * j)

        if current_sum <= C :
            max_sum = max(max_sum, current_sum)

print(max_sum)


        
