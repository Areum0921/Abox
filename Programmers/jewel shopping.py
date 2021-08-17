# deque, 윈도우 슬라이딩으로 풀려했으나 실패!
# 문제 해설보고 품
# https://tech.kakao.com/2020/07/01/2020-internship-test/
# 엥간하면 코테문제는 깔끔하고 간단하게 푸는 방법이 존재한다..
def solution(gems):

    jewel = len(set(gems)) # 보석 종류
    dict = {gems[0]:1}
    answer = [0,len(gems)-1] # 최악의 범위 (처음부터 끝)
    l,r = 0,0 # 왼쪽, 오른쪽 포인터

    while 0<=l<len(gems) and r<len(gems):
        print(dict)
        if len(dict)==jewel: # 현재 범위 내 보석 종류 개수 == 총 보석 종류 개수
            if r-l < answer[1]-answer[0]: # 기존값보다 간격이 작으면
                answer = [l,r]
            # 왼쪽 범위를 줄여보고 다시 확인해보기
            if dict[gems[l]]==1:
                del dict[gems[l]]
            else:
                dict[gems[l]]-=1
            l+=1

        else: # 오른쪽으로 범위 1 늘리기.
            r += 1
            if r == len(gems):
                break
            if gems[r] in dict:
                dict[gems[r]] += 1
            else:
                dict[gems[r]]=1

    return [answer[0]+1,answer[1]+1]







gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)