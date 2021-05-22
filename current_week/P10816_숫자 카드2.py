import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

n_dict = dict()
for card in cards:
    if card not in n_dict:
        n_dict[card] = 1
    else:
        n_dict[card] += 1

print(' '.join(str(n_dict[x]) if x in n_dict else '0' for x in numbers))