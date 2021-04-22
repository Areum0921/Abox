def solution(name):
    answer = 0
    updown = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    # A에서 위 방향으로, 아래 방향으로, 목표 알파벳까지 걸린 횟수중 작은 거 저장
    # ord('B') = 66
    # ord('A') = 65
    # ord('Z') = 90
    # B->A 아래로 내릴때 66-65 = 1
    # B->A 위로 올릴때 90-66+1 = 25
    i = 0
    while (sum(updown) != 0):
        answer += updown[i]
        updown[i] = 0
        l, r = 1, 1
        if(sum(updown)==0):
            break

        while (updown[i - l] == 0):  # 아직 완성되지않은 부분 왼쪽방향으로 찾기
            l += 1
        while (updown[i + r] == 0):  # 아직 완성되지않은 부분 오른쪽방향으로 찾기
            r += 1

        answer+= l if l < r else r # 왼쪽이 가까우면 왼쪽으로 커서이동, 반대일경우 오른쪽으로 커서이동
        i += -l if l < r else r # 왼쪽으로 이동할시, 현재 위치를 -l해서 왼쪽으로 커서이동, 반대일경우 오른쪽

    #print(answer)
    return answer

name="JAY"
solution(name)