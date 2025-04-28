a, b, c = map(int, input().split())

mul = a * b * c

def sum_mul(mul, mul_sum) :

    if mul == 0 :
        return mul_sum
    
    mul_sum += mul % 10
    return sum_mul(mul//10, mul_sum)

print(sum_mul(mul, 0))