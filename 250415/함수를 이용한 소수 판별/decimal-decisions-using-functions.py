A, B = map(int, input().split())

prime_sum = 0

def is_prime(n) :

    prime_flag = True
    for i in range(2, n) :
        if n % i == 0 :
            prime_flag = False
            break
    return prime_flag

for i in range(A, B+1) :

    if is_prime(i) :
        prime_sum += i
    
print(prime_sum)
