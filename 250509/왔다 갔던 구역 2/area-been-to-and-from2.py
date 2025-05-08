N = int(input())

current = 1000

vertical = [0 for _ in range(2001)]

commands = list()

for _ in range(N) :

    input_command = tuple(input().split())
    size = int(input_command[0])

    command = (size, input_command[1])

    commands.append(command)

for command in commands :

    for i in range(command[0]+1) :

        if commands[1] == "L" :
            vertical[current - i] += 1

        else :
            vertical[current + i] += 1

cnt = 0

for elem in vertical :

    if elem >= 2 :
        cnt += 1

print(cnt-1)



