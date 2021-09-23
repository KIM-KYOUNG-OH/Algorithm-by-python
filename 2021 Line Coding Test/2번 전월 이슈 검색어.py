def solution(research, n, k):
    issue_search_words = dict()  # 이슈검색어 저장할 dictionary
    research_dic = list()  # research to dictionary
    days = len(research)  # 일 수
    if days < n:
        return 'None'

    for data in research:
        temp = dict()
        for word in set(data):
            temp[word] = data.count(word)
        research_dic.append(temp)

    for i in range(0, days - n + 1):
        for word in research_dic[i]:
            total_search_cnt = 0  # 총 검색 횟수
            breaker = False
            for j in range(i, i + n):
                if word not in research_dic[j]:  # 이슈검색어가 되는 1번 조건 위반
                    breaker = True
                    break
                search_cnt = research_dic[j][word]  # 검색 횟수
                if search_cnt < k:  # 이슈검색어가 되는 1번 조건 위반
                    breaker = True
                    break
                total_search_cnt += search_cnt
            if breaker:
                continue
            if total_search_cnt >= (2 * n * k):  # 이슈검색어가 되는 2번 조건 체크
                if word in issue_search_words:
                    issue_search_words[word] += 1
                else:
                    issue_search_words[word] = 1

    if not issue_search_words:
        return 'None'
    # (이슈검색어가 된 횟수, 사전)순 정렬
    best_issue_search_word = sorted(issue_search_words.items(), key=lambda x: (-x[1], x[0]))
    answer = best_issue_search_word[0][0]
    return answer


print(solution(["yxxy","xxyyy","yz"], 2, 1))