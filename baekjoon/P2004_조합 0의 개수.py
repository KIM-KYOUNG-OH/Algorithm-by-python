import sys


def count_num(k, num):  # k!를 인수분해했을때 num의 개수를 리턴
    cnt = 0
    while k:
        k = k // num
        cnt += k
    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
two_cnt = count_num(n, 2) - count_num(m, 2) - count_num(n - m, 2)
five_cnt = count_num(n, 5) - count_num(m, 5) - count_num(n - m, 5)
print(min(two_cnt, five_cnt))
