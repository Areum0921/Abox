# 비트마스크 카테고리에 있으나, combinations 함수쓰면 매우 간단하다
from itertools import combinations
N,S=map(int,input().split(" "))
number=list(map(int, input().split(" ")))

sumS=0
for i in range(1,N+1):
    for j in list(combinations(number,i)):
        if(sum(j)==S):
            sumS+=1

print(sumS)
