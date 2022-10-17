def snail(snail_map):
    
    list_of_numbers = []
    
    while snail_map:
    
        for i in snail_map[0]:
            list_of_numbers.append(i)
        snail_map.pop(0)
        
        if not snail_map:
            break
                    
        for j in snail_map:
            list_of_numbers.append(j[-1])
            j.pop()
        for k in range(len(snail_map[-1]) -1, -1, -1):
            list_of_numbers.append(snail_map[-1][k])
        snail_map.pop()
        if not snail_map:
            break
        for l in reversed(snail_map):
            list_of_numbers.append((l[0]))
            l.pop(0)
        
    return list_of_numbers


    #-------------------------------------------------------

    def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


    #-------------------------------------------------------------