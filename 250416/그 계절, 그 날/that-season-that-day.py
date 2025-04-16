Y, M, D = map(int, input().split())

def is_leap_year(Y) :

    if ( Y % 4 == 0 ):

        if ( Y % 100 == 0 ) and ( Y % 400 != 0 ) :
            return False
        return True
    # 기본 리턴값
    return False

def is_exist_date(Y, M, D) :

    # 겨울
    if ( M <= 2 ) or ( M == 12 ) :

            if ( M == 2 ) :
                if is_leap_year(Y) :
                    if ( D >= 1) and ( D <= 29 ) :
                        return 4
                else :
                    if ( D >= 1 ) and ( D <= 28 ) :
                        return 4
            else :
                if ( D >= 1 ) and ( D <= 31 ) :
                    return 4
        
        # 봄
    if ( M >= 3 ) and ( M <= 5 ) :
            if ( M % 2 ) :
                if ( D >= 1 and D <= 31 ) :
                    return 1
            else :
                if ( D >= 1 ) and ( D <= 30 ) :
                    return 1
        
        # 여름
    if ( M >= 6 ) and ( M <= 8 ) :
            if ( M >= 7 ) :
                if ( D >= 1 and D <= 31 ) :
                    return 2
            else :
                if ( D >= 1 and D <= 30 ) :
                    return 2
        
        # 가을
    if ( M >= 9 ) and ( M <= 11 ) :
            if ( M % 2 ) :
                if ( D >= 1 ) and ( D <= 30 ) :
                    return 3
            else :
                if ( D >= 1 ) and ( D <= 31 ) :
                    return 3
            
    
    # 월이 아닌 경우 아예 False
    return 0

def what_season(Y, M, D) :

    if not is_exist_date(Y, M, D) :
        return -1

    if is_exist_date(Y, M, D) == 1 :
        return "Spring"
    elif is_exist_date(Y, M, D) == 2 :
        return "Summer"
    elif is_exist_date(Y, M, D) == 3 :
        return "Fall"
    else :
        return "Winter" 


print(what_season(Y, M, D))