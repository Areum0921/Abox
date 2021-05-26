# M개의 카드로 이루어진 N개의 묶음
# 하나의 카드 묶음을 선택하고 해당 묶음 안에서 가장 작은 수의 카드를 고를때 가장 큰 수는?
# 각 덱의 최소값을 찾아 비교해가며 answer 갱신
def solution(deck):
    answer=0

    for i in deck:
        if min(i) > answer: # 각 덱의 최소값을 찾아 갱신
            answer = min(i)
    print(answer)
    return answer

deck = [[3,1,2],[4,1,4],[2,2,2]]
solution(deck)