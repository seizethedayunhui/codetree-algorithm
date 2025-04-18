N = int(input())

def print_sum(N):

    if N == 0 :
        return 0
    
    return ( N % 10 )**2 + print_sum( N//10 )

ans = print_sum(N)
print(ans)