answer = 0

def dfs(numbers, target, index, value):
    global answer
    ln = len(numbers)
    if (value == target and index == ln):  # 마지막 인덱스 탐색 결과가 target일 때
        answer += 1
        return
    if (index == ln):
        return

    dfs(numbers, target, index + 1, value + numbers[index])  # 더하는경우
    dfs(numbers, target, index + 1, value - numbers[index])  # 빼는경우

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer

