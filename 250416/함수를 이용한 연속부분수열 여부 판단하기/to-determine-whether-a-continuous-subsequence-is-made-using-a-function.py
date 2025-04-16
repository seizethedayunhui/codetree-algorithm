n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def is_part_array( arr1, arr2, n1, n2 ) :

    for i in range( n1 - n2 + 1 ) :

        # 부분 flag는 계속 갱신되어야 함.
        part_flag = True

        # 내부 배열 돌기
        for j in range(n2) :
            # 하나라도 다른 부분이 있으면, 부분 수열이 될 수 없음
            if arr1[i+j] != arr2[j] :
                part_flag = False
                break
        # 부분인 경우 True 리턴
        if part_flag :
            return True
        
    return False

if is_part_array(arr1, arr2, n1, n2) :
    print("Yes")
else :
    print("No")