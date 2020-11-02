from collections import Counter

lst = []

def avg(lst):
    return round(sum(lst)/len(lst))

def mid(lst):
    temp = sorted(lst)
    return temp[len(temp)//2]
    
def often(lst):
    temp = sorted(lst)
    mode = Counter(temp)
    mod = mode.most_common()
    if len(temp)>1:
        if mod[0][1] == mod[1][1]:
            return mod[1][0]
        else:
            return mod[0][0]
    return mod[0][0]

def width(lst):
    return max(lst)-min(lst)

n = int(input())
for _ in range(n):
    lst.append(int(input()))
print(avg(lst))
print(mid(lst))
print(often(lst))
print(width(lst))
