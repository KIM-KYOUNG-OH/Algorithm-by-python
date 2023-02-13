def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    dp = [0 for _ in range(len(sticker))]  # 첫 항을 항상 뗌
    dp[0] = sticker[0]
    dp[1] = dp[0]
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    val1 = max(dp)

    dp = [0 for _ in range(len(sticker))]  # 마지막 항을 항상 뗌
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])
    val2 = max(dp)

    answer = max(val1, val2)
    return answer
