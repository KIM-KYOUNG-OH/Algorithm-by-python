lst = input().split('-')
fixed_lst = []
for i in range(len(lst)):
    temp = lst[i].split('+')
    temp_sum = 0
    for j in temp:
        temp_sum += int(j)
    fixed_lst.append(temp_sum)
answer = fixed_lst[0]
for i in range(1, len(fixed_lst)):
    answer -= fixed_lst[i]
print(answer)