# P 응시자, O는 빈테이블, X는 파티션
# 맨해튼 거리 (x1,y1) , (x2,y2)의 맨해튼 거리는 abs(x1-x2) + abs(y1-y2)
# P의 위치를 찾고 맨해튼 거리내에 다른 P가 있는지 확인.

def check(place,x,y):
    d = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,0],[1,1],[1,-1],[2,0],[-2,0],[0,-2],[0,2]]
    # 맨해튼거리 2 이내 이동 가능한 좌표 0,0은 제자리여서 제외

    for i in range(len(d)):
        a = d[i][0]+x
        b = d[i][1]+y
        if 0 <= a < 5 and 0 <= b < 5 :  # 허용되는 대기실 크기내에서 이동
            if (place[a][b] == 'P'): # 맨해튼 거리 2안에 P가 있으면
                if (abs(d[i][0]) +abs(d[i][1]) == 1):  # 맨해튼 거리가 1이면 칸막이 있을 자리 없음
                    return False
                else: # 거리가 2인곳에 P가 있을경우 사이에 칸막이 조사해야함.
                    print("칸막이 조사",x,y,a,b)
                    if(a==x): # x 좌표가 같은경우는 두좌표 y의 중간
                        if(place[a][abs(b+y)//2]=='O'):
                            return False
                    elif(b==y):
                        #print(place[abs(x+a)//2][y],a,b)
                        if(place[abs(a+x)//2][y]=='O'):
                            return False
                    else:# 두 좌표 x,y와 a,b가 모두 다를경우
                        print("??",a,y,x,b)
                        if(place[a][y]=='O' or place[x][b]=='O'): 
                            # 중간에 빈테이블 하나라도 있으면 거리두기 실패
                            return False

    return True

def solution(places):
    answer = []

    for i in places:
        chk = True
        for j in range(len(i)):
            if (chk == False): # 중간에 False가 나왔으면 끝까지 확인할 필요 x
                break
            for k in range(len(i[j])):
                if(i[j][k]=='P'): # P일때 주변 체크하기
                    print(j,k)
                    if(check(i,j,k)==False):
                        chk=False
                        break
        if(chk==False):
            answer.append(0)
        else:
            answer.append(1)
    print(answer)
    return answer

places=[["PXPOP", "XPXOX", "OOOOO", "OOXOX", "OOOOO"]]
solution(places)

"""
0 P 0 0 0
0 0 P X 0
0 0 X P 0
0 0 0 0 0
0 0 0 0 0
"""
# ["OPOOO","OOPXO","OOXPO","OOOOO","OOOOO"] -> 0 맞고
# ["PXPXP","XPXPX","OOOOO","OOOOO","OOOOO"]