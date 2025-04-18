N = int(input())

def print_sum(N) :

    if N == 1 :
        return 1
    return N + print_sum(N-1)

ans = print_sum(N)
print(ans)