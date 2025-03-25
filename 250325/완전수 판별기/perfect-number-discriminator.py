N = int(input())

measures = list()

for i in range(1, N) :

    if N % i == 0 :
        measures.append(i)

measures_sum = 0
for measure in measures :
    measures_sum += measure

if ( measures_sum == N ) :
    print("P")
else :
    print("N")