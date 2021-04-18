from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_sum = defaultdict(int) # 재생횟수 저장
    play_song = defaultdict(lambda : []) # 장르별 노래 각각 재생횟수

    i=0
    for ps,song in zip(genres,plays):
        play_sum[ps]+=song
        play_song[ps].append((i,song))
        i+=1

    sorted_play=sorted(play_sum.items(), key=lambda x:x[1], reverse=True)
    # 장르별 플레이 횟수에 따라 정렬, 내림차순


    for p in sorted_play: # 많이 재생된 장르 순
        sorted_song = sorted(play_song[p[0]], key=lambda x: x[1], reverse=True)
        # 장르별 각 곡들의 플레이횟수 내림차순
        # print(sorted_song)
        answer.append(sorted_song[0][0]) # 해당장르의 첫번째곡 삽입
        if(len(sorted_song)>1): # 해당장르 곡이 2곡이상이면
            answer.append(sorted_song[1][0]) # 2번째곡 삽입
        #print(sorted_song[0][0],len(sorted_song),sorted_song[1][0])

    print(answer)
    return answer

genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
solution(genres,plays)
