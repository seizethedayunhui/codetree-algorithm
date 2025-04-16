A, B = map(int, input().split())

def is_prime(number) :

    prime_flag = True

    for i in range(2, number) :
        if number % i == 0 :
            prime_flag = False
            return prime_flag

    return prime_flag

def is_sum_even(number) :

    num_sum = 0

    while(number > 0) :
        num_sum += number % 10
        number //= 10

    if num_sum % 2 :
        return False

    return True

def answer(A, B) :

    cnt = 0

    for i in range(A, B+1) :
        if is_prime(i) and is_sum_even(i) :
            cnt += 1
    
    return cnt

ans = answer(A, B)

print(ans)


