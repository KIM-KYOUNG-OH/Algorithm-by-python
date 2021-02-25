lst = list(map(int, input()))
length = len(lst)
a = int(length/2)

front = lst[:a]
back = lst[a:]
sum_front, sum_back = sum(front), sum(back)
if sum_front == sum_back:
    print('LUCKY')
else:
    print('READY')