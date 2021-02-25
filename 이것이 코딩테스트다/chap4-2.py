n = int(input())
cnt = 0
for i in range(3600 * (n+1)):
    lst, hours, minutes, seconds = [], [], [], []
    hour = i // 3600
    i %= 3600
    minute = i // 60
    i %= 60
    second = i
    hours.append(hour // 10)
    hours.append(hour % 10)
    minutes.append(minute // 10)
    minutes.append(minute % 10)
    seconds.append(second // 10)
    seconds.append(second % 10)
    lst.extend(hours)
    lst.extend(minutes)
    lst.extend(seconds)
    if 3 in lst:
        cnt += 1
        continue
print(cnt)
