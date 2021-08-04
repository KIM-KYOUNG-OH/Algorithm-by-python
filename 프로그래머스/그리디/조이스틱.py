# def solution(name):
#     change = [min(ord(i)-ord("A"), ord("Z")-ord(i)+1) for i in list(name)]
#     answer = 0
#     idx = 0
#     while True:
#         answer += change[idx]
#         change[idx] = 0
#         if sum(change) == 0:
#             break
#         left, right = 1, 1
#         while change[idx-left] == 0:
#             left += 1
#         while change[idx+right] == 0:
#             right += 1
#         answer += left if left<right else right
#         idx += -left if left<right else right
#
#     return answer

def get_min_alphabet_move(alp):  # 조이스틱 이동 횟수 구하기
    num = ord(alp) - 65  # 아스키코드표를 참고
    if num <= 13:
        return num
    return 26 - num  # num > 13 일 땐, 알바벳 뒤에서부터 조이스틱을 이동하는게 더 빠름


def solution(name):
    name_changed = [min(ord(name[i]) - ord('A'), ord('Z') + 1 - ord(name[i])) for i in range(len(name))]
    pos = 0  # 현재 커서 위치
    answer = 0  # 총 조이스틱 이동 횟수
    while True:
        answer += name_changed[pos]
        name_changed[pos] = 0
        if sum(name_changed) == 0:
            break
        left, right = 1, 1  # 첫 알파벳 바로 왼쪽, 오른쪽
        while name_changed[pos - left] == 0:
            left += 1
        while name_changed[pos + right] == 0:
            right += 1
        if left < right:  # 왼쪽으로 이동
            answer += left
            pos -= left
        else:  # 오른쪽으로 이동
            answer += right
            pos += right
    return answer


print(solution("JEROEN"))