N = int(input())

current = 100000
tiles = [ 0 for _ in range(200001) ]

commands = list()

for _ in range(N) :

    size, di = input().split()
    size = int(size)

    commands.append((size, di))

for command in commands :

    if command[1] == "R" :

        for i in range(command[0]) :
            tiles[current + i] = 2 # black
        current += (command[0] - 1)

    else :
        for j in range(command[0]) :
            tiles[current - j] = 1
        current -= (command[0] - 1)

W_cnt = 0
B_cnt = 0

for tile in tiles :

    if tile == 1 :
        W_cnt += 1
    elif tile == 2 :
        B_cnt += 1

print(f"{W_cnt} {B_cnt}")


