N_list = [ int(input()) for _ in range(5) ]

satisfied = True
for number in N_list :

    if number % 3 :
        satisfied = False
        break

if satisfied :
    print(1)
else :
    print(0)
