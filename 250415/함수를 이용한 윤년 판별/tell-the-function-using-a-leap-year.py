y = int(input())

def is_year(y) :

    if y % 100 == 0 :
        if y % 400 :
            return False
        else :
            return True
    if y % 4 == 0 :
        return True
    
    return False

if is_year(y) :
    print("true")
else :
    print("false")