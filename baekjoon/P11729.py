ans = []
n = int(input())

def dfs():
    if len(beams[0]) == 0 and len(beams[1]) == 0:
        return
    dfs()
    for i in range(3):
        if len(beams[i])!=0:
            for j in range(3):
                if i!=j and beams[i][-1] > beams[j][-1]:
                    beams[j].append(beams[i].pop())
                    ans.append((i,j))


beams = [[i for i in range(1, n+1, -1)], [], []]
dfs()
print(len(ans))
for i in ans:
    print(' '.join(map(str, i)))
