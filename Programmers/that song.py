# 풀이 요점 : 샵 처리방법, 라디오에서 재생된멜로디 안에 m이 있는지
def change(music): # 샵 확인
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')
    return music

def solution(m, musicinfos):

    find_list = []
    m = change(m) # 샵 처리

    for idx, i in enumerate(musicinfos):
        i = change(i)
        i = i.split(',')
        runing_time = (int(i[1][:2]) - int(i[0][:2])) * 60 + int(i[1][3:]) - int(i[0][3:])  # 해당 곡 재생 시간
        if runing_time <= len(i[3]): # 재생시간보다 곡길이가 더 길면 자르기
            melody = i[3][0:runing_time]
        else: # 재생시간보다 곡길이가 더 짧으면 실제로 재생된 반복된 멜로디 만들기
            a = runing_time//len(i[3])
            b = runing_time%len(i[3])
            melody = i[3]*a + i[3][0:b]
        if m in melody: # 들은 멜로디가 실제 재생된 멜로디 내에 포함되어있으면
            find_list.append([runing_time,idx,i[2]])

    if len(find_list)==0:
        return "None"

    answer = sorted(find_list,key = lambda x: (-x[0],x[1]))

    return answer[0][2]



m="CC#BCC#BCC#BCC#B"
musicinfos=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
solution(m,musicinfos)