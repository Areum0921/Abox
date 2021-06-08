# 순열이면 1, 아니면 0 리턴
# 중복된 값이 있으면 순열 x
# 순열 : 1~N까지 연속적으로 숫자가 1개씩

def solution(A):
    A.sort()
    length=len(A)
    max_num=max(A) # 제일 큰 수

    set_A=list(set(A))
    if length!=len(set_A): # 중복이 있어서 set_A가 더 짧아지면 순열 x
        return 0
    if A[-1]!=length: # 중복이 없지만, 순열이 아닌경우
        return 0

    return 1


A=[4,1,3]
print(solution(A))