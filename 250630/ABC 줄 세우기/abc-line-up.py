N = int(input())

arr = list(map(ord, input().split()))

cnt = 0

for i in range(1, N) :

    if (arr[i] < arr[i-1]) :

        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp

        cnt += 1

print(cnt)



