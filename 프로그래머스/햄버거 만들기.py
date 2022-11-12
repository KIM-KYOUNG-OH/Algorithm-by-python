def solution(ingredient):
    i = 0
    seq = [1, 2, 3, 1]
    l = len(ingredient)
    cnt = 0
    while True:
        if i > l - 4:
            break
        isSame = True
        for j in range(i, i + 4):
            if seq[j - i] != ingredient[j]:
                i += 1
                isSame = False
                break

        if isSame:
            ingredient = ingredient[0: i] + ingredient[i + 4:]
            cnt += 1

    return cnt