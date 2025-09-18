input_str = input()

idx = 0
for element in input_str :
    if element == "(" :
        idx += 1
    else :
        idx -= 1
    
if not idx :
    print("Yes")
else :
    print("No")
