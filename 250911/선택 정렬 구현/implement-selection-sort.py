N = int(input())

arr = list(map(int, input().split()))

for i in range(N) :
    min_idx = i

    for j in range(i+1, N) :
        if arr[j] < arr[min_idx] :
            min_idx = j

    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp

for elem in arr :
    print(elem, end=" ")