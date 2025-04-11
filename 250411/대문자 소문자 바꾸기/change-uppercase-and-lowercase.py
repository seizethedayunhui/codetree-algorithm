string = input()

for elem in string :
    if ord(elem) >= 65 and ord(elem) <= 90 :
        print(chr(ord(elem)+32), end="")
    else :
        print(chr(ord(elem)-32), end="")
