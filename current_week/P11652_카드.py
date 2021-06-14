import sys

n = int(sys.stdin.readline().rstrip())
cards = dict()  # 카드 번호: 카드 개수
for _ in range(n):
    card = int(sys.stdin.readline().rstrip())
    if card not in cards:
        cards[card] = 1
        continue
    cards[card] += 1
answer = sorted(cards.items(), key=lambda x: (x[1], -x[0]))  # 카드 개수가 같을 땐 카드 번호가 낮은 것을 뽑음
result = answer.pop()
print(result[0])
