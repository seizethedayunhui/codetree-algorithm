N = int(input())
N_list = [ int(input()) for _ in range(N) ]

for number in N_list :

    if ( number % 2 ) and ( number % 3 == 0 ) :
        print(number)