# 참고 영상 : https://www.youtube.com/watch?v=Ell5C1yoBRQ
def solution(A):
    disc=[]

    for x,y in enumerate(A): # x 중심좌표 y 반지름
        disc.append([-y+x,-1]) # 원의 왼쪽
        disc.append([y+x,1]) # 원의 오른쪽

    disc = sorted(disc)

    sect=0 # 겹치는 개수
    vals=0 # 원이 그려지기 시작했으나 다 완성되지 않은 원
    #print(disc)
    for i,j in disc:
        if j==1: # 원의 오른쪽
            vals -=1 # 원 하나 그리는거 끝났음

        elif j==-1: # 원의 왼쪽인경우
            sect += vals # 아직 그리고 있는 원 개수 -->
            # 즉 그리고 있는 원의 오른쪽이 지금 그리기 시작한 원의 왼쪽보다 뒤 -> 겹쳐지게된다.
            vals += 1 # 원하나 그리기 시작

    return sect if sect <= 10000000 else -1



A=[1,5,2,1,4,0]
solution(A)