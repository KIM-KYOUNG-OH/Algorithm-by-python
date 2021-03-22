def solution(table, languages, preference):
    totals = {'SI': 0, 'CONTENTS': 0, 'HARDWARE': 0, 'PORTAL': 0, 'GAME': 0}
    for i in range(len(table)):
        lst = table[i].split(" ")
        sub = lst.pop(0)
        lst.reverse()
        total = 0
        for j in range(len(lst)):
            for k in range(len(languages)):
                if languages[k] == lst[j]:
                    total += (j + 1) * preference[k]
                    break
        totals[sub] = total
    answer = sorted(totals.items(), key=lambda x:(-x[1],x[0]))
    return answer[0][0]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"],[7, 5]))