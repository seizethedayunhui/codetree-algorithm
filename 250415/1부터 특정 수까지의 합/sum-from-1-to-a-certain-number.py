N = int(input())

def answer(N) :

    n_sum = 0
    for i in range(1, N+1) :
        n_sum += i
    
    return int(n_sum // 10)

ans = answer(N)
print(ans)