from itertools import permutations


def solution(user_id, banned_id):
    candidates = permutations(user_id, len(banned_id))
    answer = set()
    for candidate in candidates:
        isSame = True
        for i in range(len(banned_id)):
            cur = candidate[i]
            ban = banned_id[i]
            if len(cur) != len(ban):
                isSame = False
                break

            for j in range(len(ban)):
                if ban[j] == '*':
                    continue

                if cur[j] != ban[j]:
                    isSame = False
                    break
            if not isSame:
                break

        if isSame:
            temp = tuple(sorted(candidate))
            answer.add(temp)
    return len(answer)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))