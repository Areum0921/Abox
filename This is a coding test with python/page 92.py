# 인덱스가 다른 수는 다른수로 취급
# 1개의 숫자를 연속으로 k개 까지 더할 수 있음.
# 내림차순으로 정렬후 제일큰수 k번, 그다음수 1번, 제일큰수 k번 식으로 총 m번 더하면 된다.

def solution(n,m,k):
    answer=0
    n=sorted(n,reverse=True)
    cnt=0
    for i in range(m):
        if cnt==k: # n[0]이 k번씩 더해지면
            print(n[1])
            cnt=0
        else:
            print(n[0]) # 제일 큰수 k번 더하기
            cnt+=1

    return answer

n=[3,4,3,4,3]
m=7
k=2
solution(n,m,k)