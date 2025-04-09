A = input()
B = input()

new_string1 = A + B
new_string2 = B + A

flag = 1

for i in range(len(new_string1)) :
    if new_string1[i] != new_string2[i] :
        flag = 0
        break

if flag :
    print("true")
else :
    print("false")
