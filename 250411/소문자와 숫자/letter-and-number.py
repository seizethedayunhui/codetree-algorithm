string = input()

for elem in string :
    if ord(elem) >= 97 and ord(elem) <= 122 :
        print(elem, end="")
    elif ord(elem) >= 65 and ord(elem) <= 90 :
        print(chr(ord(elem)+32), end="")
    elif ord(elem) >= 48 and ord(elem) <= 58 :
        print(elem, end="")