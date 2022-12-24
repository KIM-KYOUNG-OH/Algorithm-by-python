from itertools import permutations


def solution(numbers):
    max_num = 10 ** 7
    isPrime = [True] * max_num
    isPrime[0], isPrime[1] = False, False
    for i in range(2, int(max_num ** 0.5) + 1):
        for j in range(i + i, max_num, i):
            isPrime[j] = False

    numbers = list(numbers)
    n = len(numbers)
    numbers_set = set()
    candidates = []
    for i in range(1, n + 1):
        tmp = permutations(numbers, i)
        candidates.extend(tmp)
    for candidate in candidates:
        e = int(''.join(candidate))
        if isPrime[e]:
            numbers_set.add(e)
    print(numbers_set)
    return len(numbers_set)


print(solution('011'))