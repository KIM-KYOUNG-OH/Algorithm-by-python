n,m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
result = list()
for i in range(n):
    for j in range(i+1, n):
        if (lst[i]+lst[j]) >= m:
            continue
        else:
            for k in range(j+1, n):
                sum = lst[i]+lst[j]+lst[k]
                if sum<=m:
                    result.append(sum)
print(max(result))