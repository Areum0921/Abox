# 하노이의 탑 알고리즘 << 유명함

# n = 옮기려는 원반의 개수
# start = 옮길 원반의 현재 위치 기둥
# goal = 옮길 원반의 목표 위치 기둥
# assi = 보조 기둥
# n-1개의 원반을 assi 기둥으로 옮겨야 목표 기둥에 가장 큰 원반을 옮길 수 있다.

order=[]
def hanoi(n,start,goal,assi):
    print("n",n,"start",start,"goal",goal,"assi",assi)
    if n==1: # 1개 남았으면 goal로 이동
        print(start,"--->", goal,"이동")
        order.append([start,goal])
        return
    else:
        # 원반 n-1개를 보조기둥으로 이동 ( goal 기둥을 보조로 이용)
        hanoi(n-1,start,assi,goal)
        print(start,"--->", goal,"이동",n)
        order.append([start, goal])
        # assi로 이동해논 원반들을 goal기둥으로 이동, start 기둥을 보조로
        hanoi(n - 1, assi, goal, start)
    print("??",order)
    return order

def solution(n):
    answer=[]
    if n==1:
        return [[1,3]]

    else:
        answer=hanoi(n, 1, 3, 2)
    return answer


n=3
solution(n)

