def solution(sizes):
    row = 0
    col = 0
    # 각 카드의 긴 부분을 가로로, 짧은 부분을 세로로 정렬을 통해 취급.
    for i in range(len(sizes)):
        value = sorted(sizes[i])
        if value[0] > row:
            row = value[0]
        if value[1] > col:
            col = value[1]

    answer = row * col
    return answer

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
solution(sizes)