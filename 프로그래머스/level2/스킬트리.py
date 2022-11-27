def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        for ch in skill_tree:
            if ch not in list(skill):
                skill_tree = skill_tree.replace(ch, '')
        isPossible = True
        for i in range(len(skill_tree)):
            if skill_tree[i] != skill[i]:
                isPossible = False
        if isPossible:
            answer += 1
    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])