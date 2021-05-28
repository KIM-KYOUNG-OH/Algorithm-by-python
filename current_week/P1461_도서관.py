import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
books = list(map(int, sys.stdin.readline().rstrip().split()))
left, right = list(), list()
for i in range(len(books)):
    if books[i] > 0:
        right.append(books[i])
        continue
    if books[i] < 0:
        left.append(books[i])
left.sort()
right.sort(reverse=True)

max_value = 0  # 가장 절대값이 큰 값을 저장
for book in books:
    if abs(max_value) < abs(book):
        max_value = book

walk_cnt = []  # 왕복해야되는 경우의 수를 저장
for i in range(0, len(left), m):
    if left[i] != max_value:
        walk_cnt.append(abs(left[i]))
for i in range(0, len(right), m):
    if right[i] != max_value:
        walk_cnt.append(right[i])

answer = abs(max_value)
for cnt in walk_cnt:
    answer += 2 * cnt
print(answer)
