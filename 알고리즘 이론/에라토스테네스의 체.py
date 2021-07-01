n = 1000
is_prime = [True] * (n + 1)  # 초기화
is_prime[0], is_prime[1] = False, False
for i in range(2, int(n ** 0.5) + 1):  #
    if is_prime[i]:  # 소수일 때
        for j in range(i + i, n, i):  # 소수가 아닌 것을 지운다
            is_prime[j] = False
