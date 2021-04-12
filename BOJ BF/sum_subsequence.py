# 콤비네이션 안쓰고 리스트 안에 있는 숫자들을 조합하여 더할 수 있는 모든 경우의 값
# set 안쓰고 중복을 방지하고싶으면 False 배열을 만들고, 결과값 인덱스를 True 바꾸는 식으로 사용.
N=int(input())
s=list(map(int,input().split(" ")))
sum_list=[]

def dfs(x,y):
    if(x==N):
        sum_list.append(y)
        return

    dfs(x+1,y)
    dfs(x+1,y+s[x])

dfs(0,0)
# 결과물 sum_list.sort()하면 None으로 나옴
# sorted(sum_list)하면 정상적으로 나옴
print(sorted(set(sum_list)))