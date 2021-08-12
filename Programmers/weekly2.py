# 자신이 부여한 점수가 유일한 최저 or 최고 -> 제외

def solution(scores):
    answer = ''

    scores = list(map(list, zip(*scores)))  # 행렬 바꾸기

    for k in range(len(scores)):  # 자기 자신이 부여한 점수가 최고, 최저 점수면서 유일하면 삭제
        if scores[k][k] == min(scores[k]) or scores[k][k] == max(scores[k]):
            if scores[k].count(scores[k][k]) == 1:
                scores[k].remove(scores[k][k])

    for s in scores:
        avg = sum(s) / len(s)
        if avg >= 90:
            answer += 'A'
        elif 80 <= avg:
            answer += 'B'
        elif 70 <= avg:
            answer += 'C'
        elif 50 <= avg:
            answer += 'D'
        else:
            answer += 'F'

    return answer