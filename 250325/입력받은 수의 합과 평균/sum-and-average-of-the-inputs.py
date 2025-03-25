N = int(input())

N_list = [ int(input()) for _ in range(N) ]

sum = 0
for number in N_list :

    sum += number

ans = ( sum / len(N_list) )

print(f"{sum} {ans:.1f}")