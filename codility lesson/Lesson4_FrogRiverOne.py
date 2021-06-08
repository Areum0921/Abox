def solution(X,A):

    leaf=set() # 중복방지

    for i in range(len(A)):

        leaf.add(A[i]) # A[i] 위치에 나뭇잎 생김

        if len(leaf)==X: # 나뭇잎은 1~X까지 떨어짐.
            return i

    return -1

X=7
A=[1,5,3,4,2,5,6,3,3,7,3]
solution(X,A)


"""
def solution(X,A):

    leaf=[0]*(X+1)
    leaf[0]=1

    check=[1]*(X+1)

    for i in range(len(A)):
        if leaf[A[i]]==0: 
            leaf[A[i]]=1

        if leaf==Check:
            return i

    return -1
"""
# 같은 O(N)인데 위 코드는 시간초과
# list에서 ==는 O(N), set에서 ==는 O(len(s))
# add -> O(1)
# 파이썬 기본연산 시간복잡도 공부하기.