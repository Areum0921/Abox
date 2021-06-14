# X+1 ~ Z-1까지의 합에서 X, Y 빼기
# 첫번째 수는 합에 반드시 포함 안된다.
# X가 0이면 1번 인덱스부터 시작
# 마지막 수도 반드시 포함 안된다.
# Z가 마지막 인덱스면, 이 전 인덱스까지만 더할 수 있음.
# 1 ~ len(A)-2번 인덱스 합
# 앞부분, 뒷부분을 자를 수 있다.

def solution(A):

    left=[0]*len(A)
    rigth=[0]*len(A)


    for i in range(1,len(A)-2): # 왼쪽 슬라이스
        left[i]=max(left[i-1]+A[i],0)

    for i in range(len(A)-2,1,-1): # 오른쪽 슬라이스
        rigth[i]=max(rigth[i+1]+A[i],0)
    # 1,2,3,4,5,6일때
    # [0, 2, 5, 9, 0, 0] / [0, 0, 12, 9, 5, 0]
    # 왼쪽 0번 인덱스 + 오른쪽 2번인덱스 = 0,1,마지막인덱스
    # 0 + (3+4+5) = 12
    # 왼쪽 1번 인덱스 + 오른쪽 3번인덱스 = 0,2,마지막인덱스
    # 2 + (4+5) = 11
    # 왼쪽 2번 인덱스 + 오른쪽 4번인덱스 = 0,3,마지막인덱스
    # (2+3) + (5) = 10
    # 이런식으로 모든 인덱스 조합 중 최고값 찾기

    answer = left[0]+rigth[2]
    for i in range(1,len(A)-1):
        answer=max(answer,left[i-1]+rigth[i+1])
        print(left[i-1],rigth[i+1])

    print(left,rigth)
    return answer






A=[1,2,3,4,5,6]
solution(A)
