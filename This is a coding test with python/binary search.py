# 이진 탐색의 전제 조건 : 데이터 정렬

array = [1, 2, 3, 7, 12, 16, 17, 18, 20]

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

print(bst(array,12,0,9)) # 결과값은 해당 숫자의 인덱스 위치