t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if r1 < r2:
        r1, r2 = r2, r1
    # 두원 일치
    if distance == 0 and r1 == r2:
        print(-1)
    # 두원이 외부에 존재
    elif distance > (r1+r2):
        print(0)
    # 외접
    elif distance == (r1+r2):
        print(1)
    # 두원이 두점으로 겹침
    elif (r1-r2) < distance < (r1+r2):
        print(2)
    # 내접
    elif distance == (r1-r2):
        print(1)
    # 한원이 다른원의 내부에 존재
    elif distance < (r1-r2):
        print(0)