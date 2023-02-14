def solution(gems):
    answer = [0, len(gems) - 1]
    start, end = 0, 0
    size = len(set(gems))
    gems_dic = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        # print('start = ', start, ', end = ', end)
        if len(gems_dic) == size:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            gems_dic[gems[start]] -= 1
            if gems_dic[gems[start]] == 0:
                del gems_dic[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break

            if gems[end] in gems_dic.keys():
                gems_dic[gems[end]] += 1
            else:
                gems_dic[gems[end]] = 1
        # print('answer = ', answer)

    return [answer[0] + 1, answer[1] + 1]

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(solution(['a', 'a', 'a', 'b', 'b', 'c']))
# print(solution(['a', 'b', 'b', 'c', 'c', 'c']))
# print(solution(['a', 'b', 'b', 'c', 'c', 'c', 'a']))
# print(solution(['a', 'a', 'a', 'a']))
