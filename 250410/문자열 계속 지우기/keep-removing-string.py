A = input()
B = input()


# 문자열 안에 B가 있는 경우 계속 진행
while ( B in A ) :

    # 인덱스 에러가 발생하지 않도록 범위 설정
    for i in range(len(A)-len(B)+1) :
        flag = True
        for j in range(len(B)) :
            # 일치하는 않는 부분이 있으면 바로 break
            if A[i+j] != B[j] :
                flag = False
                break
        # B와 일치하는 부분이 중간에 있을 수도 있기 때문에 앞부분도 붙여줌
        # 1회 제거가 끝나면 len을 갱신해야하기 때문에 반복문을 벗어나도록 break 조건 설정
        if flag :
            A = A[:i] + A[i+len(B):]
            break
print(A)
