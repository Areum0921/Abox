# 경로기 때문에, 해당 지점에 왔던 여부는 중요 x. 어느 좌표에서 가는지가 중요
def solution(dirs):
    command={'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    road = set() # 경로 저장용, 중복 제거
    current_x,current_y = 0,0 # 시작 좌표
    # -5 ~ 5

    for i in dirs:
        nx = current_x + command[i][0] # 입력에 따른 좌표 이동
        ny = current_y + command[i][1]
        if -5<= nx <=5 and -5 <= ny <=5: # 이동 가능한 좌표일때
            road.add((current_x,current_y,nx,ny)) # 현재 x,y에서 다음 nx,ny로 가는 경로저장
            road.add((nx,ny,current_x,current_y)) # 반대 방향도 길은 같으므로 경로저장
            # 1경로당 2개씩 road에 저장됨
            current_x = nx # 기준 좌표 이동
            current_y = ny

    return len(road)//2
dirs="ULURRDLLU"
solution(dirs)