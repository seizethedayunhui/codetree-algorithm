N, H, T = map(int, input().split())

height = list(map(int, input().split()))

min_money = float('inf')

for i in range(N) :

    current_money = 0
    current_min_money = float('inf')

    for j in range(i, N) :

        if height[j] != H :
            current_money += abs(H-height[j])

        if (j-i+1) >= T :
            current_min_money = min(current_min_money, current_money)

    min_money = min(min_money, current_min_money)

print(min_money)
    



