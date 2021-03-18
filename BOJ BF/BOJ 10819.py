# 3 <= N <= 8 까지니까 순열 전체에 대해서 구해도 충분할듯??
from itertools import permutations
N=int(input())
number=list(map(int,input().split(" ")))
num_list=[]
max_score=0 # 최댓값
for i in list(permutations(number,N)):
    num_list.append(i)

def check(x):
    state=0
    for i in range(1,N):
        state+=abs(x[i-1]-x[i]) # 절대값
    return state

def solution():
    global max_score
    for i in range(len(num_list)):
        if(max_score<check(num_list[i])):
            max_score=check(num_list[i])


solution()
print(max_score)


