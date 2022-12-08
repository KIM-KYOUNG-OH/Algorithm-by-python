def solution(files):
    lst = []
    for file in files:
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break

                lst.append([head, number, tail])
                break

    lst = sorted(lst, key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in lst]
    return answer


solution(["F-5", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])