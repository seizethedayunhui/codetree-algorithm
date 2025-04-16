equation = list(input().split())

a = int(equation[0])
operator  = equation[1]
c = int(equation[2])


def operation(a, o, c) :

    operation_flag = True # 이 flag는 함수 안에서 선언되어야 함.

    if o == "+" :
        return a + c, operation_flag
    
    elif o == "-" :
        return a - c, operation_flag
    
    elif o == "/" :
        return int(a/c), operation_flag

    elif o == "*" :
        return a*c, operation_flag

    else :
        operation_flag = False
        return None, operation_flag

ans, flag = operation(a, operator, c)
if flag :
    print(f"{a} {operator} {c} = {ans}")
else :
    print(False)