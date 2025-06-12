N, K = map(int, input().split())

arr = list(map(int, input().split()))

min_value = float('inf')
# 최댓값 인덱스
for i in range(1, N-1) :
    max_idx = i
    current_idx = 0
    end_idx = N - 1

    flag = False
    points = list()

    for j in range(1, N) :


        if j - current_idx <= K and arr[j] <= arr[max_idx] :
            points.append(arr[j])
            current_idx = j

        if current_idx == end_idx :
            points.pop()
            flag = True
            break

    if flag :
        points.sort(reverse = True)
        min_value = min(min_value, points[0])

print(min_value)


        
