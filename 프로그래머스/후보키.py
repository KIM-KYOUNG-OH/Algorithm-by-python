from itertools import combinations

def solution(relation: list) -> int:
    col_len = len(relation[0])
    row_len = len(relation)
    candidates = []
    for i in range(1, col_len+1):
        candidates.extend(list(combinations([j for j in range(col_len)], i)))
    final = []
    for candidate in candidates:
        temp = [tuple([rel[i] for i in candidate]) for rel in relation]
        if len(set(temp)) == row_len:
            final.append(candidate)
    answer = set(final)
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))