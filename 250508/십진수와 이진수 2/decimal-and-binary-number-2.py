N = list(input())
new_N = 0

for i in range(len(N)) :
    new_N += int(N[len(N)-(i+1)]) * (2**i)

new_N *= 17

#다시 이진수로 나타내기
ans = str()
while True :

    if new_N <= 0 :
        break

    ans = str(new_N % 2) + ans
    new_N //= 2

if ans :
    print(ans)
else :
    print(new_N)

