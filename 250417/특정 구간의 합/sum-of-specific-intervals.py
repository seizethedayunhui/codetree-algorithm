N, M =map(int, input().split())

A = list(map(int, input().split()))
M_list = list()

# 범위 입력 받기
for _ in range(M) :
    a, b = map(int ,input().split())
    M_list.append((a,b))

# A를 전역변수로 활용하여 sum 구하기
def sum_arr(M_list) :
    
    for elem in M_list :
        arr_sum = 0
        arr_sum += sum(A[elem[0]-1 : elem[1]])
        print(arr_sum)

sum_arr(M_list)
