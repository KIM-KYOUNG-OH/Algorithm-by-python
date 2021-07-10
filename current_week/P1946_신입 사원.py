import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    candidates = []  # 지원자 리스트
    for _ in range(n):
        writing, talking = map(int, sys.stdin.readline().rstrip().split())  # 서류 순위, 면접 순위
        candidates.append((writing, talking))
    candidates_sorted = sorted(candidates)  # 서류 기준 정렬
    max_grade = candidates_sorted[0][1]  # idx 0번째 면접 순위 저장
    cnt = 1  # 선발할 수 있는 신입사원 최대 인원수
    for i in range(1, n):  # 0번째 항과 1을 포함한 부분 감소 수열 구하기
        if candidates_sorted[i][1] > max_grade:
            continue
        max_grade = candidates_sorted[i][1]
        cnt += 1
        if max_grade == 1:
            break
    print(cnt)
