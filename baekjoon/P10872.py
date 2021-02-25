n = int(input())

def recursive(N):
    if N == 1:
        return 1
    elif N == 0:
        return 1
    return N * recursive(N-1)

print(recursive(n))