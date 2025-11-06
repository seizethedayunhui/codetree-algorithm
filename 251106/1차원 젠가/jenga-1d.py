N = int(input())

blocks = list()
for _ in range(N) :
    element = int(input())
    blocks.append(element)

for _ in range(2) :

    start, end = map(int, input().split())
    start -= 1
    end -= 1
    temp = list()

    for i in range(len(blocks)) :
        if not (i >= start and i <= end) :
            temp.append(blocks[i])
    
    blocks = temp

print(len(blocks))
for block in blocks :
    print(block)
        
