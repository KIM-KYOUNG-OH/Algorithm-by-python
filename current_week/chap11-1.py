n = int(input())
people = list(map(int, input().split()))
count = 0
result = 0
for i in range(n):
    count += 1
    if count >= people[i]:
        result += 1
        count = 0

print(result)