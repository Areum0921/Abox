def solution(lottos, win_nums):
    answer = []

    hit = 0
    for i in lottos:
        if i in win_nums:  # 로또 번호가 당첨번호에 있으면 맞춘 숫자 +1
            hit += 1
    zero = lottos.count(0)  # 0의 개수, 최고 순위는 0의 개수만큼 더 맞출수있음.
    # print("ze",zero+hit,zero,hit)

    # 최고 순위
    if (zero + hit > 1):
        answer.append(7 - (zero + hit))  # 6개 맞췄을때 7-6 = 1등 ,5개맞췄을때 7-5 = 2등, 4개 맞췄을때 7-4=3등
    else:
        answer.append(6)  # 0개,1개는 6등임

    # 최저 순위
    if hit > 1:
        answer.append(7 - hit)  # 기존 맞춘 개수, 0가 모두 안맞았다고 생각하면 최저 등수
    else:
        answer.append(6)
    return answer