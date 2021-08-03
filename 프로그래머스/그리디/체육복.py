# def solution(n, lost, reserve):
#     reserve_del = set(reserve) - set(lost)
#     lost_del = set(lost) - set(reserve)
#
#     for i in reserve_del:
#         if i-1 in lost_del:
#             lost_del.remove(i-1)
#         elif i+1 in lost_del:
#             lost_del.remove(i+1)
#     return n-len(lost_del)

def solution(n, lost, reserve):
    # 여분의 옷을 가져온 사람이 도둑 맞았을 때: reserve와 lost의 중복 제거하기
    reserve_duplicated = list(set(reserve) - set(lost))
    lost_duplicated = list(set(lost) - set(reserve))

    for idx in reserve_duplicated:
        if (idx - 1) in lost_duplicated:  # 여분의 옷을 가진 사람 앞사람이 도둑 맞았을 때
            lost_duplicated.remove(idx - 1)
        elif (idx + 1) in lost_duplicated:  #여분의 옷을 가진 사람 뒷사람이 도둑 맞았을 때
            lost_duplicated.remove(idx + 1)
    return n - len(lost_duplicated)


print(solution(5,[2, 4],[1, 3, 5]))