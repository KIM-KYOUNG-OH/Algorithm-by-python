def is_valid(s):
    alps = [False]*26
    alps[ord(s[0])-97] = True
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        else:
            if not alps[ord(s[i])-97]:
                alps[ord(s[i])-97] = True
            else:
                return False
    return True


n = int(input())
ans = 0
for _ in range(n):
    s = input()
    if is_valid(s):
        ans+=1
print(ans)