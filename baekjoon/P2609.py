a,b = map(int, input().split())
if a < b:
    a,b = b,a
A,B = a,b
while b != 0:
    a,b = b, a%b
print(a)
lcm = (A*B)//a
print(lcm)