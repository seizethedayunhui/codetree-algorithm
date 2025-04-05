N = int(input())

num_list = list(map(int, input().split()))
max_val = float('-inf')
max_index = float('-inf')
while(max_index): 
    
    # 가장 왼쪽의 최댓값 index 출력
    for i in range(len(num_list)-1, -1, -1) :
        if num_list[i] >= max_val :
            max_val = num_list[i]
            max_index = i
    # 해당 루프까지의 max값의 index 출력
    print(max_index + 1, end=" ")
    
    # 슬라이싱 (이전 최댓값의 왼쪽에 있는 원소들만)
    # 최댓값 다시 찾아야 함으로 최댓값 초기화
    num_list = num_list[:max_index]
    max_val = float('-inf')


