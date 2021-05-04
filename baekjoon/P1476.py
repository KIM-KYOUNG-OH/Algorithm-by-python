E, S, M = map(int, input().split())
num = 1
while True:
    if num % 28 == S or (S == 28 and num % 28 == 0):
        if num % 19 == M or (M == 19 and num % 19 == 0):
            if num % 15 == E or (E == 15 and num % 15 == 0):
                break
    num += 1
print(num)