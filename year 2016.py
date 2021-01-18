def solution(a, b):
    answer = ''
    day_count=-1
    day=["FRI","SAT","SUN","MON","TUE","WED","THU",] #금요일부터 시작
    month_day=[31,29,31,30,31,30,31,31,30,31,30,31] #월별 일수
    if(a>1):
        for i in range(a-1):
            day_count+=month_day[i]
    day_count+=b

    answer=day[day_count%7]

    return answer


a=5
b=24
solution(a,b)