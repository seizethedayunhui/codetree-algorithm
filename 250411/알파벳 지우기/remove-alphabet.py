string1 = input()
string2 = input()

new_number1 = str()
new_number2 = str()

for elem in string1 :
    if ord(elem) >= 48 and ord(elem) <= 57 :
        new_number1 += elem
for elem in string2 :
    if ord(elem) >= 48 and ord(elem) <= 57 :
        new_number2 += elem

new_number1 = int(new_number1)
new_number2 = int(new_number2)

print( new_number1 + new_number2 )