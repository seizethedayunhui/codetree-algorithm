string = input()

string_len = len(string)

for i in range( string_len-1, -1, -1) :
        if i % 2 :
            print(string[i], end="")
    