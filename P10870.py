def process(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    return process(N-2) + process(N-1)

N = int(input())
print(process(N))