# def solution(genres, plays):
#     answer = []
#     # {장르 : 총 재생 횟수}
#     playDict = {}
#     # {장르 : (plays, idx)}
#     d = {}
#
#     for i in range(len(genres)):
#         genre = genres[i]
#         play = plays[i]
#         playDict[genre] = playDict.get(genre, 0) + play
#         d[genre] = d.get(genre, []) + [(play, i)]
#
#     # 재생수 기준 내림차순 정렬
#     playDict_sort = sorted(playDict.items(), key=lambda x: x[1], reverse=True)
#
#     # d에서 인기 장르순으로 하나씩 재생횟수, 인덱스으로 정렬후 두개씩 뽑기
#     for genre, totalPlay in playDict_sort:
#         d[genre] = sorted(d[genre], key=lambda x: (-x[0],x[1]))
#         answer += [idx for (play, idx) in d[genre][:2]]
#     return answer

def solution(genres, plays):
    answer = []
    play_total = dict()  # key: 장르, value: play 총합
    songs_dic = dict()  # key: 장르, value: [(고유 번호, play수)]
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in play_total:  # 첫 장르 입력시
            play_total[genre] = play
            songs_dic[genre] = [(i, play)]
            continue
        play_total[genre] += play   # play 수 더하기
        songs_dic[genre].append((i, play))

    play_sorted = sorted(play_total.items(), key=lambda x: x[1], reverse=True)  # 총 플레이수 내림차순으로 정렬
    for genre, total_play in play_sorted:
        songs_dic[genre] = sorted(songs_dic[genre], key=lambda x: (-x[1], x[0]))  # 장르별 value: 플레이수 내림차순, 고유 번호 오름차순 정렬
        answer += [idx for idx, play in songs_dic[genre][:2]]  # 장르별 두개씩만 추가
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))