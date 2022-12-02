from itertools import combinations


def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combinations([i for i in range(col)], i))

    unique = []
    for candidate in candidates:
        history = set()
        for data in relation:
            tmp = []
            for i in candidate:
                tmp.append(data[i])
            history.add(tuple(tmp))

        if len(history) == row:
            isCandidateKey = True
            for data in unique:
                if set(data).issubset(set(candidate)):
                    isCandidateKey = False
                    break

            if isCandidateKey:
                unique.append(candidate)

    return len(unique)


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])