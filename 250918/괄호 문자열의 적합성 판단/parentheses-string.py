input_str = input()

idx = 0

stack = [""] * 50
is_empty = True
flag = True

for element in input_str :

    if element == "(" :
        if is_empty :
            is_empty = False
        idx += 1

    elif element == ")" :
        if is_empty :
            flag = False
            break
        else :
            idx -= 1
        
        if not idx :
            is_empty = True

if is_empty and flag :
    print("Yes")
else :
    print("No")
        

        