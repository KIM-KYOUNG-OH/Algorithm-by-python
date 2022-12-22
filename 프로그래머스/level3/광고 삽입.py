def parse_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def parse_to_string(sec):
    h = str(sec // 3600)
    sec %= 3600
    m = str(sec // 60)
    sec %= 60
    sec = str(sec)
    return h.rjust(2, '0') + ':' + m.rjust(2, '0') + ':' + sec.rjust(2, '0')


def solution(play_time, adv_time, logs):
    logs.sort()
    play_time = parse_to_sec(play_time)
    dp = [0] * (play_time + 1)
    for log in logs:
        start, end = log.split('-')
        start = parse_to_sec(start)
        end = parse_to_sec(end)
        dp[start] += 1
        dp[end] -= 1

    for i in range(1, play_time):
        dp[i] = dp[i] + dp[i - 1]
    for i in range(1, play_time):
        dp[i] = dp[i] + dp[i - 1]

    adv_time = parse_to_sec(adv_time)
    answer = 0
    max_play = -1
    for i in range(adv_time - 1, play_time):
        tmp = dp[i] - dp[i - adv_time]
        if tmp > max_play:
            max_play = tmp
            answer = i - adv_time + 1
    return parse_to_string(answer)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))