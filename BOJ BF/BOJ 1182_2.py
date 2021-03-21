# combinations 모듈 사용 x
# combinations 사용보다 빠름 516ms -> 248ms
N,S=map(int,input().split(" "))
number=list(map(int, input().split(" ")))
cnt=0

def solution(idx,sum1):
    global cnt
    if(idx==N):
        if(sum1==S):
            cnt+=1
            return
    else:
        solution(idx+1,sum1+number[idx]) # 해당 원소를 포함하는경우
        solution(idx+1,sum1) # 포함하지 않는경우
        # 가지 뻗기
# 이런식으로 돌아감. 모든 경우에 대해서 탐색.
# 0,0 -> 1,-7 -> 2,-10
#             -> 2,-7
#     -> 1,0  -> 2,-3
#             -> 2,0
solution(0,0)
if(S!=0):
    print(cnt)
else:
    print(cnt-1)
