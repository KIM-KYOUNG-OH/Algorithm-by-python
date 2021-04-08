import sys
input = sys.stdin.readline

if __name__ == '__main__':
    arr = []
    dp = []
    n = int(input().strip())
    for _ in range(n):
        arr.append(int(input().strip()))
    dp.append(arr[0])
    if n>1:
        dp.append(max(arr[1], arr[0] + arr[1]))
    if n>2:
        dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
    for i in range(3, n):
        dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
    print(dp[-1])