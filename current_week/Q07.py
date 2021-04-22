s = input()
left = s[:len(s)//2]
right = s[len(s)//2:]
sum_left, sum_right = 0, 0
for i in range(len(s)//2):
    sum_left += int(left[i])
    sum_right += int(right[i])
if sum_left == sum_right:
    print('LUCKY')
else:
    print('READY')