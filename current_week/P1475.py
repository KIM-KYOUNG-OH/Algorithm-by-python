sets = [i for i in range(10)]
dasom = list()
n = list(map(int, list(input())))
cnt = 0
for num in n:
    if num in dasom:
        dasom.remove(num)
    else:
        if num == 6 and 9 in dasom:
            dasom.remove(9)
            continue
        elif num == 9 and 6 in dasom:
            dasom.remove(6)
            continue
        dasom = dasom + sets
        dasom.remove(num)
        cnt += 1
print(cnt)