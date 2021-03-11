# from itertools import combinations 이용하면 금방 함.
# a = [1,2,3] 인경우, combinations(a,2)는 [1,2],[1,3],[2,1],[2,3],[3,1],[3,2]에서
# [1,2] , [2,1] / [1,3],[3,1] 등의 경우 같은 배열로 취급. 즉, 처음에 1,3이 이미 나온경우 3,1은 만들지않음.
# 순서가 달라도 원소의 종류가 같으면 중복취급
N, M=map(int,input().split(" "))
check=[False]*N
result=[]

def BF(N,M):
    if(len(result)==M):
        if(99 not in result):
            print(' '.join(map(str, result)))
        return

    for i in range(N):
        if(check[i]==False):
            check[i]=True
            if(len(result)==0): # result가 비어있으면 집어넣기
                result.append(i+1)
            elif(result[len(result)-1]<i+1): # 이전에 넣은게 지금 넣으려는것보다 작으면
                result.append(i+1)
            else:
                result.append(99) # 조건에 안맞는 조합 표시
            BF(N, M)
            check[i] = False  # 11~13라인 반복하다가 7라인 리턴 발생 후 실행
            result.pop()
BF(N,M)



