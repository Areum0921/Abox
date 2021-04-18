def solution(brown, yellow):
    answer = []
    # 갈색 카펫수는 2x+2y-4
    # 노란 카펫수는 (x-2)*(y-2)
    target = brown + yellow
    i = 1
    while (1):
        j = brown - (2 * i) + 4
        if (i * (j//2) == target and i>=(j//2)): # 가로의 길이는 세로보다 길거나 같다
            if ((i - 2) * ((j//2) - 2) == yellow):
                answer.append(i)
                answer.append(j//2)
                break
        i += 1

    return answer

solution(24,24)