def solution(weights, head2head):
    answer = []
    result = []
    people = len(weights)

    for i in range(people):
        win = 0
        lose = 0
        win_heavy = 0 # 무거운 복서 상대로 승리
        for j in range(people):
            if head2head[i][j]=='W':
                win += 1
                if weights[i] < weights[j]: # 무거운애 상대로 승리했을때
                    win_heavy += 1
            elif head2head[i][j]=='L':
                lose += 1
        if win + lose == 0: # 모든 게임이 무승부
            result.append([i+1, 0, win_heavy, weights[i]]) # 선수번호, 승률, 무거운애 이긴횟수, 몸무게
        else:
            result.append([i+1, win/(win+lose), win_heavy, weights[i]])
    result = sorted(result, key = lambda x : (-x[1],-x[2],-x[3],x[0])) # 승률 높, 무거운애한테 많이 이긴, 몸무게 무거운, 앞번호

    for i in result:
        answer.append(i[0])

    return answer


weights=[50,82,75,120]	 # 복서 몸무게
head2head=["NLWL","WNLL","LWNW","WWLN"]
solution(weights,head2head)