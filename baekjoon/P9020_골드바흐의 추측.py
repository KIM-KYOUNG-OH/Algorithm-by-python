import sys

prime = [True] * 10001
prime[0], prime[1] = False, False
for i in range(2, int((10000 ** 0.5)) + 1):  # 에라토스테네스의 체
    for j in range(i * 2, 10001, i):
        prime[j] = False
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    for i in range(n // 2, 1, -1):  # 가장 먼저 나온 값이 두 소수의 값이 최소인 경우이다
        if prime[n - i] and prime[i]:
            print(i, n - i)
            break  # 골드바흐 파티션이 나오면 반복문 종료
