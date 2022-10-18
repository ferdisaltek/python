def solution(A):
    A.sort()
    p1 = A[0] * A[1] * A[-1]
    p2 = A[-3] * A[-2] * A[-1]
    print (max(p1, p2))
    return max(p1, p2)


solution([-3,1,2,-2,5,6])