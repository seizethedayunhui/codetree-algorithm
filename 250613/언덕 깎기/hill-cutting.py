N = int(input())
heights = list() # 언덕의 높이

for _ in range(N) :
    height = int(input())
    heights.append(height)

min_price = float('inf')

# 가장 낮은 언덕의 높이를 pick
for i in range(N) :

    price = 0
    for j in range(N) :

        # 차이
        diff = heights[j] - heights[i]

        # 값이 최솟값으로 지정한 값보다 작은 경우 : 그 차이만큼 곱해주면 됨
        if diff < 0 :
            price += (abs(diff) * abs(diff))
        # 값이 최솟값으로 지정한 값보다 크고, 그 차이가 17보다 큰 경우
        elif diff > 17 :
                price += (abs(diff - 17)*abs(diff - 17))

    min_price = min(min_price, price)  

print(min_price)
    


