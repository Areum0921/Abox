# 메모리 초과로 실패
# 답은 잘 나오나, N이 커질때 메모리초과
from itertools import permutations # a->b , b->a 비용이 다름, 순열

N=int(input())
city=[list(map(int, input().split(" "))) for _ in range(N)]
city_num=[i for i in range(N)] # 0~n번도시까지

route=[]
for i in list(permutations(city_num,N)): # 순회 루트
    route.append(i)

def solution():
    min_pay=999999999 # 최소비용
    for i in range(len(route)):
        print("순회 시작")
        sum = 0
        for j in range(N):
            if(j<N-1):
                if (city[route[i][j]][route[i][j + 1]] == 0):
                    continue
                else:
                    sum+=city[route[i][j]][route[i][j+1]] # 현재도시 -> 다음도시 비용
                    print(route[i], route[j],city[route[i][j]][route[i][j+1]])
            elif(j==N-1):
                sum+=city[route[i][j]][route[i][0]] # 마지막도시 -> 처음도시 비용
                print(route[i],route[j],city[route[i][j]][route[i][0]])
            print(sum,min_pay)
            if(sum>min_pay): #현재까지 비용이 이전 최소비용보다 크면 끝까지 계산할필요없다.
                print("지금까지 구한 최소비용을 넘음. 다음 루트 계산")
                break
        if(min_pay>sum):
            min_pay=sum
    return min_pay

print(solution())

