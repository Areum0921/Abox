# 다음 번 순열을 찾는 알고리즘 (나라야나 판디타)
# 1. a[i] < a[i+1] 을 만족할때, 가장큰 i값 찾기 i값이 존재하지않으면 내림차순 정렬임.
# 2. 위에서 찾은 인덱스 i 이후 a[i] < a[j]가 성립하는 j의 최대값 찾기.
# 3. i와 j자리 교환
# 4. 인덱스 i 이후값들을 오름차순으로 정렬.
N=int(input())
numlist=list(map(int, input().split(" ")))
k=-1
l=0

for i in range(1,N):
    if(numlist[i-1]<numlist[i]):
        k=i-1

if(k!=-1):
    for j in range(k+1,N):
        if(numlist[k]<numlist[j]):
            l=j
    # k <-> l 교환
    tmp = numlist[k]
    numlist[k] = numlist[l]
    numlist[l] = tmp

    a = numlist[:k + 1]  # 인덱스 0~k까지 저장
    b = numlist[k + 1:]  # 인덱스 k+1~끝까지 저장후 sort()
    b.sort()
    answer=a+b
    for i in answer: # 이어 붙이기
        print(i,end=" ")
else: # 모든 숫자가 내림차순이라는건, 사전의 맨끝이다.
    print(-1)


