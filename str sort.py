def solution(s):
    answer = ''
    s_list = list(s)

    s_list.sort(reverse=True)
    for i in s_list:
        answer+=i

    return answer

s="Zbcdefg"
solution(s)