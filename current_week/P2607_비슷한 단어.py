n = int(input())
first = list(input())
answer = 0
for _ in range(n-1):
    word = list(input())
    temp = first[:]
    for _ in range(len(word)):
        w = word.pop(0)
        if w in temp:
            temp.remove(w)
        else:
            word.append(w)
    a = len(temp)
    b = len(word)
    if (a == 0 and b == 1) or (a == 1 and b == 0) or (a == 0 and b == 0) or (a == 1 and b == 1):
        answer += 1
print(answer)