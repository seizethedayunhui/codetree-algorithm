n = int(input())

def is_number(n) :

    if ((int(n %10) + int(n//10)) % 5 == 0) and ( int(n) % 2 == 0 ) :
        return True

    return False

if is_number(n) :
    print("Yes")
else :
    print("No")