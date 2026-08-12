

n = 5
ch = 'E'

for i in range(5):

    j = 0
    while j <= i:
        print(chr(ord(ch)+j) , end="")
        j+=1

    print()

    ch = chr(ord(ch)-(1))


