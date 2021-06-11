# A 요소는 unique하다.
# 하류로 가는 물고기 체크

def solution(A,B):
    stack=[]
    cnt = 0

    for i in range(len(A)):
        if B[i]==1: # 하류로 가는 물고기
            # 1번물고기가 상류,하류를 가든 2번물고기는 1번물고기보다 시작점이 더 하류에 있기때문.
            # 그래서 하류로 가는경우 앞번호 물고기들을 만날 가능성 0
            # 3번물고기가 하류 , 4번물고기가 하류 -> 같은방향 만날일 없음.
            # 3번물고기가 상류, 4번물고기가 하류 -> 3번물고기는 4번물고기보다 더 상류 위치에서 상류로가는것. 만날일 없음.
            stack.append(A[i])

        else: # 상류로 가는 물고기 -> 더 상류에서 하류로 내려오는 물고기들과 비교
            for j in range(len(stack)-1,-1,-1):
                if stack[j] > A[i]: # 지금물고기가 상류로 가는데 하류로 내려오는 물고기중에 더 큰놈만남
                    break
                else: # 하류로 내려오는 작은 물고기 만남, 잡아먹기
                    stack.pop()
            if len(stack)==0:# 상류로가는데 하류로 내려오는 물고기가 더이상 없으면 물고기 수 +1
                print(stack,A[i])
                cnt+=1

        print("남은 물고기", stack,cnt)
    return cnt+len(stack)





A=[2,4,3,5,7,8,9,10]
B=[0,1,0,1,0,0,0,1]
print(solution(A,B))