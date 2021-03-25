def solution(skill, skill_trees):
    count = len(skill_trees)
    for tree in skill_trees:
        skill_lst = list(skill)
        for i in range(len(tree)):
            temp = tree[i]
            if temp in skill_lst:
                first_alp = skill_lst.pop(0)
                if temp!=first_alp:
                    count-=1
                    break

    return count