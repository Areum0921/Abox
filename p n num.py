def solution(s):
    answer = True
    string=s.lower()
    p = 0
    y = 0

    for i in range(len(string)):

        if (string[i] == 'p'):
            p += 1
        elif (string[i] == 'y'):
            y += 1

    if (p != y):
        answer = False

    return answer

s="Pyy"
solution(s)