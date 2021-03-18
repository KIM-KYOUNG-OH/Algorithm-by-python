def solution(n):
    count = 1
    for i in range(1, n//2+1):
        total = 0
        for j in range(i,n+1):
            total += j
            if total==n:
                count+=1
                break
            if total>n:
                break
    return count