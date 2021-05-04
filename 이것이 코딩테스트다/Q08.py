s = input()
alp = []
number = []
for i in s:
    if 48 <= ord(i) <= 57:
        number.append(int(i))
    else:
        alp.append(i)
print(''.join(sorted(alp)) + str(sum(number)))