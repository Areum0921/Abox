def solution(s):
    answer = ''
    lists = s.split(" ")
    # print(lists)
    for i in range(len(lists)):
        lists[i] = int(lists[i])

    answer += str(min(lists))
    answer += " " + str(max(lists))

    return answer