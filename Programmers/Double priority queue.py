import heapq

def solution(operations):
    answer = []
    order = [i.split(" ") for i in operations]

    for i in order:
        # print(i[0],i[1],i[1][0])
        if (i[0] == 'I'):
            heapq.heappush(answer, int(i[1]))  # heappush로 값넣으면 알아서 정렬된다.

        elif (i[0] == 'D' and len(answer) > 0):  # 명령어가 D고
            if (i[1][0] == '-'):  # 숫자가 음수면 heappop을 이용해 최소값 삭제
                heapq.heappop(answer)
            else:
                answer.pop()  # 숫자가 양수면 최대값인 맨뒤값 삭제

    if (len(answer) == 0):
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    # print(answer)
    return answer

operations=		["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
solution(operations)