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



print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))