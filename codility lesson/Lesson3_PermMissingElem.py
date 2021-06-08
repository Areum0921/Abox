def solution(A):
    A.sort()

    if len(A) == 0:  # 1~1 array = [] --> 1..(N+1) --> [1]
        return 1
    elif len(A) == 1:  # 1~2 array=[1] --> 1..(N+1) --> [1,2]
        if A[0]==1:
            return 2
        else: # array[2] --> [1,2]
            return 1
    else:
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
            if i == (len(A) - 1):  # 마지막까지 missing element가 없는경우
                return i + 2