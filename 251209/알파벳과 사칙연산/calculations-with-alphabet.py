equation = input()

operations = list()
elements = list()
element_list = list()
element_dict = {}

N = len(equation)

for e in equation :
    if e == "*" or e == "+" or e == "-" :
        operations.append(e)
    else :
        elements.append(e)
        if not e in element_list :
            element_list.append(e)

M = len(element_list)


def calc_equation() :

    calc_current = 0

    for i in range(len(elements)) :
        element_num = element_dict[elements[i]]
        # 연산기호
        if i :
            if operations[i-1] == "*" :
                calc_current *= element_num
            elif operations[i-1] == "+" :
                calc_current += element_num
            else :
                calc_current -= element_num
        else :
            calc_current = element_num
        # print(calc_current)
    return calc_current



def complete_equation(idx) :
    
    if idx == M :
        cur = calc_equation()
        # print(element_dict)
        # print(element_list)
        # print(cur)
        return cur

    max_ans = float('-inf')

    for i in range(4) :
        e = element_list[idx]
        element_dict[e] = (i+1)
        max_ans = max(max_ans, complete_equation(idx+1))

    return max_ans

    
ans = complete_equation(0)
print(ans)
