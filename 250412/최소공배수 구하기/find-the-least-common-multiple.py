n, m = map(int, input().split())

def gcd(n, m) :

    if (m == 0) :
        return n
    else :
        return gcd(m , n%m)

print( (n*m) // gcd(n,m) )