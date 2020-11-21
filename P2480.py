lst = sorted(list(map(int, input().split())))

result = 0
if len(set(lst)) == 1:
    print(10000 + 1000 * lst[0])
elif len(set(lst)) == 2:
    print(1000 + 100 * lst[1])
else:
    print(100 * lst[2])
