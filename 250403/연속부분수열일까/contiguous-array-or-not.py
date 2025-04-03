n1, n2 = map(int, input().split())

n1_arr = list(map(int, input().split()))
n2_arr = list(map(int, input().split()))


for i in range(n1) :
    flag = 1
    for j in range(n2) :
        # 인덱스 범위 벗어나는 경우 + 바깥배열의 값과 안의 배열이 다른 경우 flag 바꾸고 break
        if (i+j >= n1) or n1_arr[i+j] != n2_arr[j]:
            flag = 0
            break
    # flag가 1이면 이미 부분집합이라는걸 확인했으므로 더 이상 반복할 필요가 없음. 
    if flag :
        break
if flag :
    print("Yes")
else :
    print("No")
            