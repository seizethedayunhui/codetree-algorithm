
for i in range(19) :
    for j in range(19) :
        if (j+1) != 19 and (j+1) % 2 :
            print(f"{i+1} * {j+1} = {(i+1)*(j+1)}", end=" / ")
        else :
            print(f"{i+1} * {j+1} = {(i+1)*(j+1)}")
    