n,m=map(int,input().split(' '))
a_list,b_list=list(), list()
for i in range(m):
    a,b=map(int, input().split(' '))
    a_list.append(a)
    b_list.append(b)

numbers = [i for i in range(n)]
while b_list:
    i=b_list[0]
    numbers.remove(a_list[0])
    numbers.insert(i-1,a_list[0])
    a_list.pop[0]
    b_list.pop[0]
for i in numbers:
    print(i, end=" ")