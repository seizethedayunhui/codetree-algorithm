N, K = map(int, input().split())

arr = list(map(int, input().split()))

min_price = float('inf')

# i 인덱스에 있는 값이 최소가 되도록 함. 
for i in range(1, 10000) :

    current_price = 0
    ranges = [i, i+ K]

    for j in range(N) :

        if arr[j] < ranges[0] :
            current_price += abs(ranges[0] - arr[j])
        elif arr[j] > ranges[1] :
            current_price += abs(ranges[1] - arr[j])
    
    min_price = min(min_price, current_price)

print(min_price)
