import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
lst = sorted(list(set(numbers)))
lst_dic = dict()
for i in range(len(lst)):
    lst_dic[lst[i]] = i
for num in numbers:
    print(str(lst_dic[num]), end=' ')
