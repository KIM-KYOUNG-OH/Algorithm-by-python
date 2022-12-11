def solution(n, words):
    prev = words[0][0]
    history = set()
    for i in range(len(words)):
        cur = words[i]
        if cur[0] != prev or cur in history:
            rnd = (i // n) + 1
            idx = (i % n) + 1
            return [idx, rnd]
        prev = cur[-1]
        history.add(cur)
    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))