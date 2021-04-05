def recursive(n):
    global matrix
    if n == 3:
        matrix[0][:3] = matrix[2][:3] = [1,1,1]
        matrix[1][:3] = [1,0,1]
        return
    a = n//3
    recursive(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                matrix[a*i+k][a*j:a*(j+1)] = matrix[k][:a]


n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
recursive(n)
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            print('*', end='')
        else:
            print(' ', end='')
    print()