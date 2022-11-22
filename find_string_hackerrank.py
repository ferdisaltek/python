def count_substring(string, sub_string):
    c=0
    l_sub=len(sub_string)
    for i in range(0,len(string)):
        if sub_string ==string[i:i+l_sub]:
            c+=1
    return c



count_substring(input("string : "),input("sub_String : "))