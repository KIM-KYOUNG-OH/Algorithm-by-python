s = input()
name_cnt = [0] * 26
for alp in s:
    name_cnt[ord(alp)-65] += 1
odd = 0
odd_alp = ''
alps = ''
for i in range(26):
    alp_cnt = name_cnt[i]
    if alp_cnt > 0:
        if alp_cnt % 2 == 1:  # 해당 알파벳이 홀수개 이면
            odd += 1
            odd_alp += chr(i + 65)  # 가운데에 하나만 위치시킴
        alps += chr(i + 65) * (alp_cnt // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alps + odd_alp + alps[::-1])