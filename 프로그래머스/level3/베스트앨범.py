from collections import defaultdict


def solution(genres, plays):
    genre_dic = defaultdict(list)
    genre_lst = []
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in genre_dic:
            for j in range(len(genre_lst)):
                c, g = genre_lst[j]
                if g == genre:
                    genre_lst[j][0] += play
                    break
        else:
            genre_lst.append([play, genre])

        genre_dic[genre].append([play, i])

    for key in genre_dic.keys():
        genre_dic[key] = sorted(genre_dic[key], key=lambda x: (-x[0], x[1]))
    genre_lst.sort(reverse=True)

    answer = []
    for cnt, genre in genre_lst:
        limit = 2
        for play, id in genre_dic[genre]:
            if limit == 0:
                break
            answer.append(id)
            limit -= 1
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
