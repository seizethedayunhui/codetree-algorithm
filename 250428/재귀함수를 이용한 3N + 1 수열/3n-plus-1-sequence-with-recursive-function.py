N = int(input())

def solution(N, cnt) :

    if N == 1 :
        return cnt

    if N % 2 :
        return solution( 3 * N + 1, cnt + 1 )
    
    else :
        return solution( N // 2 , cnt + 1 )

print(solution(N, 0))
