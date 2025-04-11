A = input()
req_list = input()

for req in req_list :
    if req == 'L' :
        A = A[1:]+A[0]
    else :
        A = A[-1]+A[:-1]
print(A)