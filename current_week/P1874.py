n = int(input())
nums = [i for i in range(n, 0, -1)]
stack = [0]
ans = []
for _ in range(n):
    request = int(input())
    if request == stack[-1]:
        ans.append('-')
        stack.pop()
        continue
    elif request in nums:
        while True:
            num = nums.pop()
            stack.append(num)
            ans.append('+')
            if num == request:
                stack.pop()
                ans.append('-')
                break
    else:
        ans = ['NO']
        break

for i in ans:
    print(i)