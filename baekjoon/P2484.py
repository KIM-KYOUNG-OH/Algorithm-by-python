def grading(lst):
    if len(set(lst)) == 1:
        return 50000 + 5000*lst[0]
    elif lst[0]==lst[1] and lst[2]==lst[3]:
        return 2000 + 500*lst[0] + 500*lst[3]
    elif len(set(lst)) == 2:
        return 10000+1000*lst[1]
    elif len(set(lst)) == 3:
        for i in range(3):
            if lst[i]==lst[i+1]:
                return 1000+100*lst[i]
    else:
        return 100*lst[3]

N = int(input())
result = list()

for _ in range(N):
    lst = sorted(list(map(int, input().split())))
    result.append(grading(lst))
    
print(max(result))