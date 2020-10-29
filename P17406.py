def judge(lst):
    temp = []
    for i in lst:
        temp.append(sum(i))
    return min(temp)

def r(r,c,s):
    global lst
    

N,M,K = map(int, input().split())

lst = [list(map(int, input().split())) for i in range(N)]

for _ in range(k):
    r,c,s = map(int, input().split())

