def solution(n, a, b):
    round_num = 1
    leagues = [0]
    for i in range(1, n + 1):
        participant = list()  # (순서, 정체)
        if i == a:
            participant = [i, 'A']
        elif i == b:
            participant = [i, 'B']
        else:
            participant = [i, 'N']  # Doesn't matter
        leagues.append(participant)

    while len(leagues) != 2:
        after_leagues = [0]
        for i in range(1, len(leagues), 2):
            prev_idx, prev_who = leagues[i][0], leagues[i][1]
            next_idx, next_who = leagues[i + 1][0], leagues[i + 1][1]
            if prev_who in ['A', 'B'] and next_who in ['A', 'B']:
                return round_num
            elif prev_who == 'N' and next_who in ['A', 'B']:
                after_leagues.append([next_idx // 2, next_who])
            elif prev_who in ['A', 'B'] and next_who == 'N':
                after_leagues.append([next_idx // 2, prev_who])
            else:
                after_leagues.append([next_idx // 2, 'N'])
        leagues = after_leagues
        round_num += 1


print(solution(8, 4, 7))