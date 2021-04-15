import sys
input = sys.stdin.readline

n = int(input())
ans = []
lst = []
for i in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))
for i in range(n):
    rank = 1
    for j in range(n):
        if j == i:
            continue
        else:
            if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
                rank += 1

    ans.append(rank)

print(" ".join(map(str, ans)))