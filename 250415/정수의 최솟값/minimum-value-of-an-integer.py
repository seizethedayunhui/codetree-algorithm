a, b, c = map(int, input().split())

def select_min(a, b, c) :

    if a < b and a < c :
        return a
    elif b < a and b < c :
        return b
    else :
        return c

ans = select_min(a, b, c)
print(ans)