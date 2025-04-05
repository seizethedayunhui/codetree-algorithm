N = int(input())
price_list = list(map(int, input().split()))
profit = 0

for i in range(N) :
    for j in range(i, N) :
        current_profit = price_list[j] - price_list[i]
        if current_profit > profit :
            profit = current_profit

print(profit)