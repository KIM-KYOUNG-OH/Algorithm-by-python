n, k = map(int, input().split())
lst = [i+1 for i in range(n)]
ans = []
idx = 0
for _ in range(n):
    idx += k-1
    if idx >= len(lst):
        idx %= len(lst)
    ans.append(lst.pop(idx))

print('<',end='')
print(', '.join(map(str, ans)), end='>')