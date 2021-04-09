import sys
input = sys.stdin.readline

n = int(input())
number_cnt = [0] * 10001
for _ in range(n):
    number_cnt[int(input())] += 1
for i in range(10001):
    if number_cnt[i] != 0:
        for _ in range(number_cnt[i]):
            sys.stdout.write('%s\n' % i)
