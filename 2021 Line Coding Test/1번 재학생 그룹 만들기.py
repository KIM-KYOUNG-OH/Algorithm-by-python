def solution(student, k):
    answer = 0
    old = student.count(1)  # 재학생 수
    if k > old:  # 애초에 재학생이 부족할 때
        return answer

    for start in range(len(student)):  # start는 그룹 시작지점
        old_cnt = 0  # 매 케이스마다 재학생 수
        for end in range(start, len(student)):  # end는 그룹 종료지점
            current = student[end]  # 현재 학생
            if current == 0:  # 신입
                if old_cnt == k:  # 그룹 만들기 가능
                    answer += 1
            elif current == 1:  # 재학생
                if old_cnt < k:
                    old_cnt += 1
                    if old_cnt == k:  # 그룹 만들기 가능
                        answer += 1
                elif old_cnt >= k:  # end 이후로 그룹 만들기 불가능
                    break

    return answer


print(solution([0, 1, 0], 2))