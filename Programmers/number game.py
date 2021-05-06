# 이게 3레벨은 아닌듯
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    print(A,B)
    j=-1
    for i in range(len(A)-1,-1,-1): # 큰 숫자부터 비교
        if A[i]<B[j]: # 현재 A의 제일큰 숫자보다 B의 제일큰 숫자가 더 클때 이길 수 있음.
            answer+=1
            j-=1
        # 현재 A[i]보다 큰 숫자가 B에 없을땐 이길수 없는 숫자.
    print(answer)

    return answer


A=[5,1,3,7]
B=[2,2,6,8]
solution(A,B)