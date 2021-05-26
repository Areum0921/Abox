# 나이트가 이동할 수 있는 방법은 L자형으로 8가지
# 수평 2칸 + 수직 1칸
# 수직 2칸 + 수평 1칸
# 말판 = 8x8 1~8
def solution(loc):
    answer=0
    loc=[ord(loc[0])-96,int(loc[1])] # 알파벳 좌표 숫자로 전환
    dx=[[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]] # 움직일 방향

    for i in dx:
        if 0<loc[0]+i[0]<9 and 0<loc[1]+i[1]<9: # 이동한 위치가 말판 범위 내면
            answer+=1 # 이동가능 횟수 카운트
    print(answer)
    return answer


loc='g5'
solution(loc)