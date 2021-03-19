# 백트래킹 이용하기
# 그러나 시간이 오래걸린다. 찾아보니 대부분 비트마스크 기법을 사용한다.
def solution(start,current,cost): # 시작점, 현재위치, 가격
    global min_pay,now_pay,check
    if (start==current and check.count(False) == 0):
        # 현재위치가 시작점이면서 모든곳을 방문했을때-->시작점으로 돌아오는것 포함 모든 곳을 순회 했을때임
        # 중간에 시작도시로 돌아오는경우도 있으므로 check.count(False)==0 필요
        print("현재루트 비용:",cost,"새로운 루트 탐색 시작")
        paylist.append(cost)
        min_pay=min(min_pay, cost)

    for i in range(N):

        if (city[current][i]!=0 and check[i]==False):# 거리비용이 0이 아니고 방문하지않은 도시일때
            # 거리비용이 0이면 현재도시에서 현재도시로 이동이다.
            check[i]=True # 방문체크하고
            print("?", start,current, i, city[current][i],check)
            # 시작 도시는 다른도시 -> 시작도시 일때 방문체크된다.
            solution(start,i,cost+city[current][i]) # 해당도시로 가는 비용을 cost에 더해준다.
            check[i]=False
N=int(input())
city=[list(map(int, input().split(" "))) for _ in range(N)]
check=[False]*N
paylist=[]
min_pay=999999999 # 각 행렬원소의 최대값이 100만인것을 감안해서 크게 잡아야한다.
solution(0,0,0) # 싸이클이라 0에서 시작하는것만 봐도된다.
#ex) 0 1 2 3 0  , 0->1, 1->2, 2->3, 3->0 거리들의합
# 1 2 3 0 1 , 1->2, 2->3, 3->0, 0->1 거리들의합.
# 거리들의 합 구성이 똑같은걸 알 수 있다.
print(min_pay)
print(paylist)


