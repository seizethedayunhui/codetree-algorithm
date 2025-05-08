A, B = map(int, input().split())
N = list(input())


new_N = 0
for i in range(len(N)):
    new_N += int(N[len(N) - (i+1)]) * (A ** i)


ans = str()

while True :

    if new_N <= 0 :
        break
    
    ans = str(new_N % B) + ans
    new_N //= B
    
if ans :
    print(ans)
else :
    print(new_N)