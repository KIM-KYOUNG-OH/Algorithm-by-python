s = input()
temp = s[0]
cnt = 0
for i in s[1:-1]:
    if i != temp:
        temp = i
        cnt += 1
ans = cnt//2 + cnt%2
print(ans)