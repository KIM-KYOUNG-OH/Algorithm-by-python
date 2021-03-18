def solution(info, query):
    answer = []
    for question in query:
        cnt = len(info)
        temp = list(question.split(' '))
        while 'and' in temp:
            temp.remove('and')
        for i in range(len(info)):

            grade = info[i].split(' ')[-1]
            if int(grade) < int(temp[-1]):
                cnt -= 1
                # print("점수 미달 - cnt : ", cnt)
                continue
            for j in range(4):
                # print(temp[j])
                if temp[j] == "-":
                    continue
                if temp[j] not in info[i]:
                    cnt -= 1
                    # print("cnt : ", cnt)
                    break

        answer.append(cnt)
        # print(answer)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))