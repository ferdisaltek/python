def swap_case_fonk(s):
    swap=""
    for i in s:
        
        if i.islower()==True:
            i=i.upper()
            swap+=i
        elif i.isupper()==True:
            i=i.lower()
            swap+=i
    #print(swap)
    return swap

def swap_case(s):
    return s.swapcase()


swap_case('HackerRank.com presents "Pythonist 2".')
