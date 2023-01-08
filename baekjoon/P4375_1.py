import sys

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        i = 0
        num = 0
        while True:
            num = num * 10 + 1
            i += 1
            if num % n == 0:
                print(i)
                break
    except:
        break
