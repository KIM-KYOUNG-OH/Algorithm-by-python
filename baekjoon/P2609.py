def find_yak():
    for i in range(low):
        yak = low - i
        if low % yak == 0 and high % yak == 0:
            return yak

def find_bae():
    for i in range(high, high*low+1):
        bae = high+i
        if bae%high == 0 and bae%low == 0:
            return bae

a,b = map(int, input().split())
low, high = 0, 0
if a<b:
    low, high = a, b
else:
    low, high = b, a
print(find_yak())
print(find_bae())