N = int(input())

def Fibonacci(N):

    if N == 1 :
        return 1
    if N == 2 :
        return 1
    
    return Fibonacci(N-1) + Fibonacci(N-2)

ans = Fibonacci(N)

print(ans)