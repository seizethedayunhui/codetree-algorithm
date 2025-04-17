A = input()

def same_cnt(A) :

    cnt_arr = []
    
    for elem in A :
        flag= True
        for i in range(len(cnt_arr)) :
            if cnt_arr[i] == elem :
                flag = False
                break
        if flag :
            cnt_arr.append(elem)

    if len(cnt_arr) >1 :
        return True
    return False

if same_cnt(A) :
    print("Yes")
else :
    print("No")
        
