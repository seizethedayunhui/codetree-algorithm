N, M = map(int, input().split())

seq = list()
def make_seq(elem, seq_len) :

    if seq_len == M :
        for elem in seq :
            print(elem, end=" ")
        print()
        return
    
    for i in range(elem, N+1) :
        seq.append(i)
        make_seq(i+1, seq_len+1)
        seq.pop()

make_seq(1, 0)
