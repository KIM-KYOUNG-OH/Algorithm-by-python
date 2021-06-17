def next_permutation(n):
    l = len(n)
    x = 0  # highest index
    for i in range(l - 1):
        if n[i] < n[i + 1]:
            x = i
    if x == 0:
        return -1  # 다음 순열이 없다는 것을 의미
    for j in range(l - 1, 0, -1):
        if n[j] > n[x]:
            n[x], n[j] = n[j], n[x]
            break
    return n[:x + 1] + n[:x:-1]


s = [2, 5, 1, 9, 7]
print(next_permutation(s))
