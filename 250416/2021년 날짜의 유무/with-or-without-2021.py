M, D = map(int, input().split())

def is_exist_date(M, D) :

    if M >= 1 and M <= 12 :

        if ( M == 2 ) and ( D >= 1 and D <= 28 ) :
            return True
        elif M <= 7 :
            if ( M % 2 ) and ( D >=1 and D <= 31 ) :
                return True
            elif ( D >= 1 and D <= 30 ) :
                return True
        else :
            if ( M % 2 == 0 ) and ( D >=1 and D <= 31 ) :
                return True
            elif ( D >= 1 and D <= 30 ) :
                return True

        return False
    
    return False

if is_exist_date(M, D) :
    print("Yes")
else :
    print("No")