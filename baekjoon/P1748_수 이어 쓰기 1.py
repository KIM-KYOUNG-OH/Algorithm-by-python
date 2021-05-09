n = int(input())
length = len(str(n))  # n은 몇자리 수 인가
memo = [0] * length  # length-1 자리수까지 각 자리수들의 합
answer = 0
for i in range(1, length):
    memo[i] = 9 * (10 ** (i - 1)) * i
temp = length * (n - 10 ** (length - 1) + 1)  # 최대 자릿수들의 개수 * length
answer = sum(memo) + temp
print(answer)