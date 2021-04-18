n = int(input())
dic = dict()
ans = [0] * n
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for idx, num in enumerate(b):
    dic[idx] = num
b_sorted = sorted(dic.items(), key=lambda x:x[1])
a.sort()
for i in b_sorted:
    temp = a.pop()
    ans[i[0]] = temp
result = 0
for i in range(n):
    result += (ans[i] * b[i])
print(result)