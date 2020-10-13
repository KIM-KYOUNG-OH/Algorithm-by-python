N,M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team, num = input(), int(input())
    team_mem[team] = []

    for j in range(num):
        mem = input()
        mem_team[mem] = team
        team_mem[team].append(mem)

for i in range(M):
    name, q = input(), int(input())
    if q:
        print(mem_team[name])
    else:
        for i in sorted(team_mem[name]):
            print(i)