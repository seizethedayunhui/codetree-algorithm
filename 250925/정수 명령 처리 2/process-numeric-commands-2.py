from collections import deque

def cmd(queue, command) :

    if command[:4] == "push" :
        command, element = command.split()
        queue.append(int(element))
    elif command == "pop" :
        left = queue.popleft()
        print(left)
    elif command == "size" :
        print(len(queue))
    elif command == "empty" :
        if len(queue) :
            print(0)
        else :
            print(1)
    else :
        print(queue[0])
            
N = int(input())
queue = deque()

for _ in range(N) :
    command = input()
    cmd(queue, command)

