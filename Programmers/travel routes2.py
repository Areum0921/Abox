# 주어진 항공권을 모두 사용하는 루트를 짜야함
# 다른 곳으로 갈수없는 공항들부터 배열에 넣어줌.
# stack
def solution(tickets):
    tickets = sorted(tickets, key=lambda x: x[1], reverse=True)  # 도착지 기준 정렬 pop(0)보다 pop()이 시간이 덜 듦

    answer = []
    routes = dict()

    for i in tickets: # i[0]공항에서 갈수있는 공항들 넣기.
        if i[0] in routes:
            routes[i[0]].append(i[1])
        else:
            routes[i[0]] = [i[1]] # dict 초기값을 list로 넣으면 append 가능

    start = ['ICN']  # 인천 출발

    while start:
        print("출발가능한 공항 순서", start)

        cur = start[-1] # stack

        if cur not in routes or len(routes[cur]) == 0: # 현재 공항에서 갈 수 있는곳이 없으면 answer에 추가.
            answer.append(start.pop())
        else:
            # 현재 공항에서 갈 수 있는 다른 공항이 있다면 stack에 추가.
            start.append(routes[cur].pop())
        print("루트", answer)
    print(answer)

    return answer

tickets=[["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
solution(tickets)