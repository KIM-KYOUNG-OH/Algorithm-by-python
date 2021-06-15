# import heapq
# import sys
#
# grades = []
# total = 0
# answer = []
# for i in range(1, 9):
#     grade = int(sys.stdin.readline().rstrip())
#     heapq.heappush(grades, (-grade, i, grade))
# for _ in range(5):
#     max_grade = heapq.heappop(grades)
#     total += max_grade[2]
#     answer.append(max_grade[1])
# answer.sort()
# print(total)
# print(' '.join(map(str, answer)))

import sys

grades = []
total = 0
answer = []
for i in range(1, 9):
    grade = int(sys.stdin.readline().rstrip())
    grades.append((i, grade))
grades = sorted(grades, key=lambda x: x[1])
for i in range(3, 8):
    total += grades[i][1]
    answer.append(grades[i][0])
answer.sort()
print(total)
print(' '.join(map(str, answer)))