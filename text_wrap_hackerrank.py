import textwrap

def wrap(string, max_width):
    print(string)
    l=len(string)
    for i in range(0,l,max_width):
        print(string[i:i+max_width])

    #return textwrap.fill(string,max_width)

    


wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4)


