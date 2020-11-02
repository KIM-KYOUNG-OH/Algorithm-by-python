from collections import Counter

def often(lst):
    cnt = Counter(lst)
    cnt_lst = cnt.most_common()
    print(cnt_lst)
    if len(cnt_lst)>1:
        if cnt_lst[0][1] == cnt_lst[1][1]:
            return cnt_lst[1][0]
        else:
            return cnt_lst[0][0]
    else:
        return cnt_lst[0][0]


n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
print(often(lst))

