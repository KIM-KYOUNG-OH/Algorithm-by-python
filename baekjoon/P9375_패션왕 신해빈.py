import sys

t = int(sys.stdin.readline().rstrip())  # 테스트 갯수
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cloth = dict()  # 해시
    for _ in range(n):
        cloth_name, kind = sys.stdin.readline().rstrip().split()  # 의상 이름, 종류
        if kind not in cloth:
            cloth[kind] = 1
            continue
        cloth[kind] += 1
    cloth_counts = cloth.values()  # 종류별 의상 갯수
    answer = 1
    for i in cloth_counts:
        answer *= (i + 1)
    print(answer - 1)  # 아무것도 안입은 경우를 뺌
