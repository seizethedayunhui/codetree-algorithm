X, Y = map(int, input().split())

cnt = 0
for num in range(X, Y+1) :

    digits = [0] * 10
    all_digits = 0

    while (num != 0) :
        digits[num % 10] += 1
        all_digits += 1
        num //= 10

    interesting = False

    for digit in digits :

        if digit == all_digits - 1 :
            interesting = True

    if interesting : cnt += 1


print(cnt)

