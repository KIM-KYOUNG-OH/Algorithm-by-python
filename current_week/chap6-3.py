n = int(input())
dic = dict()
for _ in range(n):
    name, grade = input().split()
    dic[name] = int(grade)
ans = sorted(dic.items(), key=lambda x:x[1])
for i in ans:
    print(i[0], end=" ")