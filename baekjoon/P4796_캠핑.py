import sys

i = 0
while True:
    i += 1
    L, P, V = map(int, sys.stdin.readline().rstrip().split())
    if L == 0 and P == 0 and V == 0:
        break
    possible_days = (V // P) * L + min((V % P), L)
    print("Case " + str(i) + ": " + str(possible_days))
