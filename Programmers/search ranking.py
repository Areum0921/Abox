# bisect 사용법 숙지하기
# 정렬된 리스트 a에 x를 삽입할 위치를 알려줌
# bisect_left 는 왼쪽 인덱스, bisect_right는 오른쪽 인덱스
from itertools import combinations
from bisect import bisect_left

def make_all_cases(con): # 지원자 별로 해당 지원자가 통과할 수 있는 모든 경우의 조건 만들기
    cases = []
    for k in range(5): # 필요한 조합 정보는 4가지 언어, 직군, 경력, 소울 푸드
        for li in combinations([0, 1, 2, 3], k): # 점수 제외 0~3개모든 경우 조합 인덱스 0~3
            # 0개~4개 일치 경우
            case = ''
            for idx in range(4):
                if idx not in li: # 조합에 있는 숫자가 없으면 -
                    case += '-'
                else: # 해당하는 숫자있으면 con에 해당하는 조건 넣기.
                    case += con[idx]
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all={}
    for i in info: #
        sep_info = i.split() # 공백으로 info 정보 나누기
        print(sep_info)
        cases = make_all_cases(sep_info) # 해당 정보로 통과 가능한 조건 조합 만들기
        for case in cases: # 통과 가능한 조건들을 하나씩 꺼내 검사
            print("???",case)
            if(case not in all.keys()): # make_all에서 만든 키에 case가 없을때 -> 점수임
                all[case] = [int(sep_info[4])] # 통과가능한 케이스를 키로, 값을 점수로
            else:
                all[case].append(int(sep_info[4])) # 키로 만든게 있으면 점수 info 점수 넣기

    for j in all.keys(): # 점수를 기준으로 오름차순
        # 각 키값 조건에 해당하는 지원자의 점수들
        all[j].sort()
    #print(all)

    for q in query:
        seperate_q = q.split() # 쿼리 분리
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6] # and,점수 제외하고 합치기
        print("sqsq",seperate_q[7])
        if target in all.keys(): # query 기준으로 만들어낸 target이 아까 지원자 기준으로 만든 모든 경우의수 중에 있다면
            print("@#?",all[target],bisect_left(all[target], int(seperate_q[7]), lo=0, hi=len(all[target])))
            # 키 target에 해당하는 점수개수에서, 해당 쿼리의 점수보다 낮은 부분의 인덱스 위치를 뺀다.
            # ex) all[target] = [10,30,50,110,160] (정렬되어있을때)
            # seperate_q[7] = 100이면
            # bisect_left(all[target] , seperate_q[7], lo=0, hi=len(all[target])) 일때
            # all[target]에 100을 삽입할 위치는 10,30,50, **100**, 110,160 로, 인덱스 3을 리턴한다.
            # 그러면 5개중 3개를 빼면 100이상의 숫자가 남은 개수와 똑같다.
            answer.append(len(all[target]) - bisect_left(all[target], int(seperate_q[7]), lo=0, hi=len(all[target])))
            # 정렬된 전체경우에서 기준점수보다 낮은경우 빼기
        else:# all.keys()에 없다면 조건에 맞는게 없다.
            answer.append(0)

    print(answer)
    return answer

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
#query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
query=["java and backend and junior and pizza 100"]
solution(info,query)
