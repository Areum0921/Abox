# 시간을 분단위로 변경해서 계산하기
def solution(n, t, m, timetable):
    answer = ''
    start=540 # 시작시간 9시는 540분
    line_time=[]
    bus_time=[540]
    for i in range(n-1): # n회 운행하는 버스 출발 시간표
        start+=t
        bus_time.append(start)
    #print("버스시간표",bus_time)
    for i in timetable:
        line_time.append(int(i[0]+i[1])*60+int(i[3]+i[4])) # 줄서는 시간을 분으로 환산
    line_time.sort()

    for i in range(n):

        if len(line_time) < m: # 남은 크루가 태울수 있는 인원보다 적으면
            print('%02d:%02d' % (bus_time[-1]//60,bus_time[-1]%60))
            return '%02d:%02d' % (bus_time[-1]//60,bus_time[-1]%60)

        if i == n-1: # 마지막 배차일때 마지막으로 타는사람보다 1분앞
            if line_time[m-1] <= bus_time[i]: # m번째 승객이 마지막 버스를 탈 수 있으면
                # 해당 승객보다 1분앞
                print('%02d:%02d' % ((line_time[m-1]-1) // 60, (line_time[m-1]-1) % 60))
                return '%02d:%02d' % ((line_time[m-1]-1) // 60, (line_time[m-1]-1) % 60)
            else: # 마지막 배차일때 빈자리 남으면 해당버스시간
                return '%02d:%02d' % (bus_time[i]//60,bus_time[i]%60)

        for j in range(m): # m명씩 현재 버스 시간전에 온사람 순서대로  태우기
            # 마지막 배차 아님.
            if bus_time[i]>=line_time[j]:
                del line_time[j] # 태운 크루 삭제
n=2
t=10
m=2
timetable=["09:10", "09:09", "08:00"]
solution(n,t,m,timetable)
