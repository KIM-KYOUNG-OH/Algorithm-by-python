x = int(input())
sticks = [64]
while True:
    if sum(sticks) == x:
        print(len(sticks))
        break
    stick = sticks.pop()
    sticks.append(stick // 2)
    if sum(sticks) < x:
        sticks.append(stick // 2)
