def mutate_string(string, position, character):
    s=string[:position]+character+string[position+1:]
    return s


mutate_string("abracadabra",5,'k')