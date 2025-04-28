n = int(input())

n_list = list(map(int, input().split()))

max_n = n_list[n-1]

def max_recursion(n, max_n):

    if n == 0 :
        return max_n
    
    if n_list[n-1] >= max_n :
        max_n = n_list[n-1]

    return max_recursion(n-1, max_n)

print(max_recursion(n, max_n))



