def permutation(s):
    sonuc = ""
    r=len(s)
    for i in range(r):
        sonuc += s-i
    return sonuc



permutation("selam")