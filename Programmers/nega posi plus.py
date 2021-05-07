def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)): # absolutes 수만큼 signs
        if (signs[i] == True): # i번째 수의 sign을 확인하고
            answer += absolutes[i] # True면 양수 +
        else:
            answer -= absolutes[i] # False면 음수 -

    return answer