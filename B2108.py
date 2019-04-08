import sys
from collections import Counter

N=int(sys.stdin.readline())

slist=[]

for i in range(N):
    slist.append(int(sys.stdin.readline()))

slist.sort()#오름차순리스트 저장

find=Counter(slist).most_common() #빈도 많은순으로 find에 저장

freq=find[0][1] #가장 빈도수 많은 숫자(같을경우 작은수가 먼저옴)
#[i][j]일때 i는 반복되는 숫자, j는 숫자의 반복횟수
counts=[]
for i in find: #find안에서 freq와 같은 빈도수 찾기.
    if i[1]==freq: #빈도(반복횟수) 같으면 
        counts.append(i[0])#해당빈도에 해당하는 숫자를 리스트에 추가.


print(round(sum(slist)/N))#산술평균
print(slist[N//2])#중앙값

if len(counts)>1: # 최빈값이 1개초과일때 2번째가 최빈값
    print(counts[1])
    
else:
    print(counts[0])# 최빈값이 1개이하일때 첫번째가 최빈값

print(slist[-1]-slist[0])#오름차순으로 정렬된리스트에서 맨마지막값-맨처음값



   
    
    
