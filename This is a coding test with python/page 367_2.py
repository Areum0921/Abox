# 이진탐색 구현

N,x = map(int,input().split(" "))
a = list(map(int,input().split(" ")))

def start(a,s,e,t): # a, start, end, target  , target이 시작되는 지점 찾기.
    if s > e:
        return None
    mid = (s+e)//2

    if a[mid]==t and (a[mid-1] < t or mid==0): # a[mid]값이 찾는값이고, mid이전값은 찾는값보다 작거나, mid값이 0이면
        return mid
    elif a[mid] >= t:
        return start(a,s,mid-1,t)
    else:
        return start(a,mid+1,e,t)

def last(a,s,e,t): # 마지막 target의 위치
    if s > e:
        return None
    mid = (s+e)//2

    if a[mid] == t and (a[mid+1]>t or mid==e):
        return mid
    elif a[mid] <= t:
        return last(a,mid+1,e,t)
    else:
        return last(a,s,mid-1,t)

def solution(a, s, e, t):
    first = start(a,s,e,t)
    if first == None:
        return -1
    end = last(a,s,e,t)

    return end-first+1

print(solution(a,0,N-1,x))