def solution(begin, target, words):
    if target not in words:  # target이 words안에 없으면 변환 불가
        return 0
    answer = 0  # 변환 횟수
    search_scope = [begin]  # 탐색 범위
    candidates = []  # 글자 차이가 하나로, 가능한 모든 경우
    visited = [False for _ in range(len(words))]
    while search_scope:
        for wd in search_scope:
            candidates.clear()
            for idx, word in enumerate(words):
                if visited[idx]:
                    continue
                diff = 0  # 글자 차이 수
                for i in range(len(word)):
                    if wd[i] != word[i]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:  # wd와 한글자 차이인 word는 candidates에 추가
                    candidates.append(word)
                    visited[idx] = True
        answer += 1
        if target in candidates:
            break
        search_scope = candidates[:]
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))