from collections import deque


def isChangable(a, b):
    same_cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            same_cnt += 1
    if same_cnt == len(a) - 1:
        return True
    else:
        return False





def solution(begin, target, words):
    def dfs(visited, i, cnt):
        cur = words[i]
        if cur == target:
            if 1 <= cnt < answer[0]:
                answer[0] = cnt
            return

        for j in range(len(words)):
            if not visited[j] and isChangable(cur, words[j]):
                visited[j] = True
                dfs(visited, j, cnt + 1)
                visited[j] = False


    answer = [11]
    for i in range(len(words)):
        word = words[i]
        if isChangable(begin, word):
            visited = [False] * len(words)
            visited[i] = True
            dfs(visited, i, 1)
    if answer[0] == 11:
        return 0
    else:
        return answer[0]


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
