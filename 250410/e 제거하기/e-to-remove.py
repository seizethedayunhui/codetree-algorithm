string = input()

for i in range(len(string)) :
    if string[i] == 'e' :
        string = string[:i]+string[i+1:]
        break
print(string)