from wsgiref.util import request_uri


def solution(a):
    if len(a)==1:
        return 0
    if len(a)==0:
        return -1
    half=len(a)/2
    #print(half)
    count_number=[]
    for i in a:
        count_number.append(a.count(i))
    m=max(count_number)
    if max(count_number)>half:
        return count_number.index(m)
    else:
        return -1



solution([3,4,3,2,3,-1,3,3])