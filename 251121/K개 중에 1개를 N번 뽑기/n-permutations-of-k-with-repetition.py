K, N = map(int, input().split())

pair = list()

def print_pairs(arr) :
    for e in arr :
        print(e, end=" ")
    print()

def find_pairs(k) :

    if k == K + 1 :
        return

    pair.append(k)

    for i in range(1, K+1) :
        pair.append(i)
        depth(1, i)

    pair.pop()
    find_pairs(k+1)
    

def depth(n,i) :

    if n == N + 1:
        print_pairs(pair)
        pair.pop()
        return 

    depth(n+1, i)



find_pairs(1)
        