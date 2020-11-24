n, m, k = map(int, input().split())
lst = list(map(int, list(input().split())))
lst.sort()
a = lst[len(lst)-1]
b = lst[len(lst)-2]
print((b+k*a)*(m//(k+1)) + a*(m%(k+1)))

