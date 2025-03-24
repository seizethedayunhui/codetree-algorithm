A, B, C = map(int, input().split())

if A > B :
    # A가 가장 큰 경우
    if A > C :
        if B > C :
            print(B)
        else :
            print(C)

# B가 가장 큰 경우
if B > C :
    if B > A :
        if A > C :
            print(A)
        else :
            print(C)
# C가 가장 큰 경우
if C > B :
    if C > A :
        if A > B :
            print(A)
        else : 
            print(B)


    
    