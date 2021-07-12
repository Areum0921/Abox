# NlogN으로 구현하기
# 모든 원소는 오름차순
# 이진 탐색 트리, 중간값이 중간인덱스값보다 큰지 작은지 판단
def search(arr,start,end):
    print("state",arr,start,end)
    if start > end:
        return None
    mid = (start + end) // 2 # 중간인덱스
    print("mid",arr[mid],mid)
    if arr[mid] == mid: # mid인덱스에 위치한값 == mid
        return mid
    elif arr[mid] > mid: # 중간에 있는 숫자보다 위치한 인덱스가 더 큰 수면 뒷부분에서 탐색
        return search(arr, start, mid-1)
    else: # 반대의 경우 앞부분에서 다시 탐색
        return search(arr, mid +1,end)

def solution(arr,start,end):
    first = search(arr, start, end)
    if first == None: # 조건에 맞는 값을 못찾으면 -1 리턴
        return -1
    return first

arr=[-23,-10,-4,-2,4]
answer = solution(arr,0,len(arr)-1)

print(answer)
