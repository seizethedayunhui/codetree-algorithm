N = int(input())
cnt = 0

def ex_cnt(N, cnt) :

    if N == 1 :
        return cnt
    
    if N % 2 :
        return ex_cnt(N//3, cnt+1)
    else :
        return ex_cnt(N//2, cnt+1)

ans = ex_cnt(N, 0)
print(ans)



