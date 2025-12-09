equation = input()

operations = list()
elements = list()

N = len(equation)

for e in equation :
    if e == "*" or e == "+" or e == "-" :
        operations.append(e)
    else :
        elements.append(e)


M = len(elements)


def calc_equation() :

    calc_current = 0

    for i in range(M) :
        # 연산기호
        if i :
            if operations[i-1] == "*" :
                calc_current *= elements[i]
            elif operations[i-1] == "+" :
                calc_current += elements[i]
            else :
                calc_current -= elements[i]
        else :
            calc_current = elements[i]
    return calc_current



def complete_equation(idx) :

    
    if idx == M :
        return calc_equation()

    max_ans = float('-inf')

    for i in range(4) :
        elements[idx] = (i+1)
        max_ans = max(max_ans, complete_equation(idx+1))

    return max_ans

    

ans = complete_equation(0)
print(ans)
