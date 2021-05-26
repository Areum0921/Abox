# n-1 or n/k 를 반복해 최소 횟수로 1만들기
# n/k는 나누어 떨어질때만 가능
# 최대한 나누면서 1씩 빼면된다.
def solution(n,k):
    cnt=0
    while n!=1:
        if n%k==0:
            n=n/k
            cnt+=1
        else:
            n-1
            cnt+=1
    print(cnt)
    return cnt

n=25
k=5
solution(n,k)