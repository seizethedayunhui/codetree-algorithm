N = int(input())
arr = list(map(int, input().split()))
min_diff = float('inf')

for i in range(N) :

    remaining_arr = list()
    for j in range(N) :

        if i == j :
            continue

        for k, elem in enumerate(arr):
            if k == i :
                remaining_arr.append(elem*2)
            elif k != j :
                remaining_arr.append(elem)

    diff = 0
    for l in range(N-2) :
        diff += abs(remaining_arr[l] - remaining_arr[l+1])
    
    min_diff = min(min_diff, diff)

print(min_diff)
