A = input()

def compare_str(A) :
    
    new_A = str()
    
    for i in range(len(A)-1, -1, -1) :
        new_A += A[i]
    
    if A == new_A :
        return True
    return False

if compare_str(A) :
    print("Yes")
else :
    print("No")