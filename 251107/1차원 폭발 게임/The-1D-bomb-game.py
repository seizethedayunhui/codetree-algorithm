N, M = map(int, input().split())

arr = [ int(input()) for _ in range(N)]

flag = True

while flag :

    current_len = len(arr)

    temp = list()
    for i in range(current_len) :
        temp.append(arr[i])
        
    current_element = arr[0]
    cnt = 0
    start_idx = 0

    for i in range(len(arr)) :

        if arr[i] == current_element  :
            cnt += 1
        else :
            end_idx = i

            if cnt >= M :
                for j in range(start_idx, end_idx) :
                    temp[j] = 0
            
            current_element = arr[i]
            start_idx = i
            cnt = 1

    # 마지막으로 한 번 더 체크
    if cnt >= M :
        for j in range(start_idx, current_len) :
            temp[j] = 0

    new_arr = list()
    for k in range(current_len) :
        if temp[k] :
            new_arr.append(arr[k])
    arr = new_arr 

    # while 문 계속 돌아가는 조건
    """
    1. 이전과 비교해서 변화가 있었을 경우
    2. 현재 폭탄의 개수가 폭탄 터지는 조건 이상일 경우
    """
    flag = (len(arr) != current_len and len(arr) >= M)


print(len(arr))
for element in arr :
    print(element)
