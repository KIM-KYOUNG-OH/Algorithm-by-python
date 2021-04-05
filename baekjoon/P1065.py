n = int(input())
ans = 0

def is_right(lst):
    diff = lst[1]-lst[0]
    for j in range(1, len(lst)-1):
        if lst[j+1] - lst[j] != diff:
            return False;
    return True


for i in range(1, n+1):
    if i<100:
        ans+=1
    else:
        lst = list(map(int, list(str(i))))
        if is_right(lst):
            ans+=1

print(ans)