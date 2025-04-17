N, M = map(int, input().split())
A = list(map(int, input().split()))

def print_number(A, N, M) :
    answer = 0
    while (M >= 1) :

        answer += A[M-1]

        if M % 2 :
            M -= 1
        else :
            M //= 2
    return answer

ans = print_number(A, N, M) 
print(ans)