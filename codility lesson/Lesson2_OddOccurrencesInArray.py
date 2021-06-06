def solution(A):
    if len(A)==1: # 숫자가 하나인경우
        print("unpair",A[0])
        return A[0]
    A.sort() # 정렬후 같은숫자 세가면서 비교
    cnt=1

    for i in range(1, len(A)):

        if A[i - 1] == A[i]:
            cnt += 1
        else:
            print(A[i - 1], A[i], cnt, i)
            if cnt % 2 == 0:
                cnt = 1
                if i==len(A)-1: # 마지막 숫자만 남았을때
                    print("unpair",A[i])
                    return A[i]
            else:
                print("unpair", A[i-1])
                return A[i-1]



#A=[3,9,3,9,9,7,9]
A=[3]
solution(A)