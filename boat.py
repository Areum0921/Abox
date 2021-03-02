#최대 2명만 태울수있음!!
#조건을 제대로 보지않아 3명,4명 태우는경우까지 생각하느라 시간 날렸다. 풀기전 조건을 제대로 확인하자.

def solution(people, limit):
    people.sort()# 몸무게가 가벼운순으로 정렬후 , 가벼운사람+가능한 무거운사람 조합으로한다.
    b_cnt=0 # 보트 수
    r=0 #오른쪽방향
    l=len(people)-1 #왼쪽방향

    while(r <= l):# 양옆으로 줄여오면서 limit에 걸리지않는 최대합 구하기
        if (people[r]+people[l] > limit): # 태울수 없을때
            l-=1
        else: # 태울수있을때 , 2명태우고 무게가 남아도 다음보트 조합구하기, 최대 2명만 탈수있음!
            r+=1
            l-=1
        b_cnt+=1 # 보트 개수 증가

    print(b_cnt)
    return b_cnt



people=[50,50,50]
limit = 50
solution(people, limit)
