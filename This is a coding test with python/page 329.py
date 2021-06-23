# 방법 접근 성공

# 가능한 구조물인지 체크
def check(answer):
    for x,y,a in answer:
        if a==0: # x,y좌표의 기둥이 존재할 수 있는지
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False

        elif a==1: # x,y좌표의 보가 존재할 수 있는지
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

    return True

def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x,y,a,b = i

        if b==1: # 설치시
            answer.append([x,y,a]) # 일단 설치
            if not check(answer): # 가능한가?
                answer.remove([x,y,a]) # 불가능시 삭제

        else:
            answer.remove([x,y,a]) # 일단 삭제
            if not check(answer): # 가능한가?
                answer.append([x,y,a]) # 불가능시 되돌리기

    return sorted(answer)



n=5
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(n,build_frame)