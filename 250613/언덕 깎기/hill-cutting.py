N = int(input())
heights = list() # 언덕의 높이

for _ in range(N) :
    height = int(input())
    heights.append(height)

min_price = float('inf')

# 가장 낮은 언덕의 높이를 pick
for i in range(101) :

    price = 0
    # list에 포함되지 않는 다른 높이인 경우에도 가능할 수 있음. 
    ranges = [i, i + 17]

    for j in range(N) :

        if heights[j] < ranges[0] :
            price += (abs(ranges[0] - heights[j]) ** 2)
        elif heights[j] > ranges[1] :
            price += (abs(heights[j] - ranges[1]) ** 2)

    min_price = min(min_price, price)  

print(min_price)
    


