a, b = map(int, input().split())

def square(a, b) :

    answer = 1

    for _ in range(b) :
        answer *= a
    
    return answer

ans = square(a, b)
print(ans)