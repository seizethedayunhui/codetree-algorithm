N = int(input())

def odd_even(N) :

    if N <= 2 :
        return N
    return N + odd_even(N-2)

print(odd_even(N))