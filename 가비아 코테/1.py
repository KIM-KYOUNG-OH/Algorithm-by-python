def solution(n: int) -> int:
    result = 1
    for i in range(1,n+1):
        result *= i
    num = 1
    cnt = 1
    while result%num == 0:
        cnt += 1
        num *= 10

    return cnt

print(solution(10))