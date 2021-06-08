def solution(A):
    A=list(set(A)) # 중복 제거

    A.sort() # 정렬
    print(A)

    if max(A)<0:
        print(1)
        return 1

    else:
        cnt=1
        for i in range(len(A)):
            if A[i]>0: # 1~ 찾기
                if A[i]!=cnt:
                    print(cnt)
                    return cnt
                cnt+=1

            if i==len(A)-1:
                print(cnt)
                return cnt

A = [-3,-2,-3,-5,-8,-7,-1,1]
solution(A)