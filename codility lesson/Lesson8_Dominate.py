# 절반이상 등장한 요소의 인덱스중 하나만 출력하면된다.
# 빈리스트, 리스트요소 1개인경우도 처리해줘야한다.
# 가능한 경우를 모두 고려하자.

import operator

def solution(A):
    length = len(A)
    dict = {}

    if length<1: # 요소가 없으면 dominator x
        return -1
    if length==1: # 요소가 한개면 절반(0.5개)이상이므로 반드시 0번 인덱스가 dominator
        return 0

    for i in A: # 각 숫자들이 몇번씩 등장했는지 체크하기.
        if i in dict:
            dict[i] += 1
        else:
            dict[i]=1

    occur=sorted(dict.items(),key=operator.itemgetter(1)) # 각 숫자들이 나온 횟수순으로 1번 인덱스 기준으로 오름차순 정렬

    if occur[-1][1]>length//2:
        for i in range(len(A)):
            if A[i]==occur[-1][0]:
                return i
    else:
        return -1

A=[3,4,3,2,3,-1,3,3]
solution(A)