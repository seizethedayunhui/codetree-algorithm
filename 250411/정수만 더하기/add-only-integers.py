A = input()

int_sum = 0
for elem in A :
    if ord(elem) >= 48 and ord(elem) <= 57 :
        int_sum += int(elem)
print(int_sum)