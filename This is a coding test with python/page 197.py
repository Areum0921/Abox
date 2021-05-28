# in 사용안하고 이진 탐색 코드를 구현해 풀어보기

def bst(array, target, start, end):
    if start > end: # 찾을수없음.
        return False

    mid = (start + end) // 2 # 중간지점

    if target==array[mid]: # 찾고자 하는 숫자와 mid 인덱스에 해당하는 숫자가 같으면 찾기 성공.
        return mid

    elif target > array[mid]: # 찾는값이 중간값보다 크면 중간값 다음 수 ~ 마지막 탐색
        return bst(array,target,mid+1,end)
    else: # 찾는값이 중간값보다 작으면 시작~중간값-1 까지 다시탐색
        return bst(array,target,start,mid-1)

def solution(N,M):
    N=sorted(N) # 정렬

    for i in M:
        if bst(N,i,0,len(N)-1)==False:
            print("No",end=" ")
        else:
            print("Yes",end=" ")

N=[8,3,7,9,2]
M=[5,7,9]
solution(N,M)
