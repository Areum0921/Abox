# 장르별 노래 2개씩!

from collections import defaultdict

def solution(genres, plays):
    answer = []

    play_sum = defaultdict(int)
    song_play = defaultdict(lambda : []) # 장르별 노래 각각 재생횟수
    i=0

    for gen,play in zip(genres,plays):
        play_sum[gen]+=play # 해당 장르의 플레이 횟수
        song_play[gen].append((i,play)) # 각 노래가 속하는 장르와, 몇번째 노래인지
        i+=1

    play_sum = sorted(play_sum.items(), key = lambda x:x[1],reverse=True) # 플레이 횟수로 내림차순

    for i in play_sum: # song_play에서 key값(장르명)들 이용하기 많이 재생된 장르부터
        print("sdsds",i)
        #song_play[i]는 각 장르별 (곡번호, 재생횟수) 출력
        sorted_song = sorted(song_play[i[0]], key=lambda x:x[1],reverse=True) # i 장르에서 플레이 횟수가 많은 순으로 내림차순
        print(sorted_song)

        answer.append(sorted_song[0][0])
        if len(sorted_song) > 1:  # 해당 장르 곡이 2개 이상이면
            answer.append(sorted_song[1][0])  # 2번째 곡의 곡번호도 추가


    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
solution(genres,plays)