def solution(word, pages):
    names = []
    links = dict()
    basic_score = dict()
    result = dict()
    for i in range(len(pages)):
        page = pages[i]
        idx = page.find('content=\"')
        idx += 17
        url = ''
        while page[idx] != '"':
            url += page[idx]
            idx += 1
        names.append(url)

        # 기본 점수
        fixed_page = page.lower()
        word_lower = word.lower()
        bs = 0
        while fixed_page.find(word_lower) != -1:
            idx = fixed_page.find(word_lower)
            if not fixed_page[idx - 1].isalpha() and not fixed_page[idx + len(word_lower)].isalpha():
                bs += 1
            fixed_page = fixed_page[:idx] + fixed_page[idx + len(word_lower):]
        basic_score[url] = bs

        # 링크 수
        links_tmp = []
        temp = page.split('<a href=\"https://')
        if len(temp) > 1:
            for j in range(1, len(temp)):
                str = temp[j]
                idx = 0
                link = ''
                while str[idx] != '"':
                    link += str[idx]
                    idx += 1
                links_tmp.append(link)
        links[url] = links_tmp

    print(basic_score)
    print(links)
    for i in range(len(names)):
        name = names[i]
        score = 0
        for link in links[name]:
            temp = basic_score[link] / len(links[link])
            print(temp)
            score += temp
        result[i] = score

    max_val = max(result.values())
    answer = 0
    for i in range(len(result)):
        if result[i] == max_val:
            answer = i
    return answer


print(solution("bind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))