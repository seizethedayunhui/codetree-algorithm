N = int(input())
arr = list(map(int ,input().split()))


def merge_sort(low, high, arr) :

    mid = (low + high) // 2

    if (low < high) :

        merge_sort(low, mid, arr) #아랫부분 정렬
        merge_sort(mid+1, high, arr) # 윗부분 정렬

    merge(low, mid, high, arr)


sorted_arr = [ 0 for _ in range(N) ]

def merge(low, mid, high, arr) :

    i = low
    j = mid+1

    k = low

    while (i <= mid or j <= high) :

        # 둘 다 가능한 경우
        if (i <= mid and j <= high) :

            if (arr[i] <= arr[j]) :
                sorted_arr[k] = arr[i]
                i += 1
            else :
                sorted_arr[k] = arr[j]
                j += 1

        # 둘 중 하나만 가능한 경우
        elif (i <= mid) :
            sorted_arr[k] = arr[i]
            i += 1
        else :
            sorted_arr[k] = arr[j]
            j += 1
        
        k += 1

    for idx in range(low, high+1):
        arr[idx] = sorted_arr[idx]


merge_sort(0, N-1, arr)

for elem in arr :
    print(elem, end=" ")

        