n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input())
ans = 64
for i in range(n-7):
    for j in range(m-7):
        first_B = 0
        first_W = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if matrix[k][l] != 'B':
                        first_B += 1
                    else:
                        first_W += 1
                else:
                    if matrix[k][l] != 'W':
                        first_B += 1
                    else:
                        first_W += 1
        ans = min(ans, first_B, first_W)

print(ans)