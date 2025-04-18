N = int(input())

def print_hello_word(str, N):

    if N == 0 :
        return
    print_hello_word(str, N-1)
    print(str)

print_hello_word("HelloWorld", N)

