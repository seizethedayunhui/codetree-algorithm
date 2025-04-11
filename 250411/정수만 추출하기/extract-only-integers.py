string1, string2 = input().split()

new_number1 = str()
new_number2 = str()

for elem in string1 :
    if ord(elem) >= 48 and ord(elem) <= 57 :
        new_number1 += elem
    else :
        break
new_number1 = int(new_number1)

for elem in string2 :
    if ord(elem) >= 48 and ord(elem) <= 57 :
        new_number2 += elem
    else :
        break
new_number2 = int(new_number2)

print( new_number1 +  new_number2 )
