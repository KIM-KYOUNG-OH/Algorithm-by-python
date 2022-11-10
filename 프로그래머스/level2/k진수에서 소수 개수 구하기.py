def parse(n, k):
    result = ''
    while n:
        share = n // k
        remainder = n % k
        result = str(remainder) + result
        n = share
    return result


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    s = parse(n, k)
    arr = s.split('0')
    while arr.count(''):
        arr.remove('')
    s_list = list(map(int, arr))

    cnt = 0
    for tmp in s_list:
        if isPrime(tmp):
            cnt += 1

    return cnt


solution(1100011, 10)