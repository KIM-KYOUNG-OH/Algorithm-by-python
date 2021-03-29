def solution(s:str)->int:
    alps = set()
    for i in range(1, len(s)+1):
        n = len(s)-i
        for j in range(n+1):
            word = s[j:j+i]
            skip = 0
            if len(word)>1:
                alp_before = set([word[0]])
                for k in range(1, len(word)):
                    if word[k] in alp_before:
                        skip = 1
                        break
                    else:
                        alp_before.add(word[k])
            if skip == 1:
                continue
            alps.add(word)

    return len(alps)

print(solution("abac"))