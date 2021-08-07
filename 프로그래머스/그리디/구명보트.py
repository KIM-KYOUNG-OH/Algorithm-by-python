# def solution(people, limit):
#     people_sorted = sorted(people, reverse=True)
#     count = len(people_sorted)
#     start, end = 0, len(people_sorted)-1
#     sum = 0
#     while start < end:
#         sum += start+end
#         if sum <= limit:
#             end -= 1
#             count -= 1
#         else:
#             sum = 0
#         start += 1
#
#     return count

def solution(people, limit):
    people.sort(reverse=True)
    start, end = 0, len(people) - 1
    boat_cnt = len(people)  # 필요 보트 수를 미리 사람수 만큼 확보
    while start < end:
        # 가장 무거운 사람 + 가장 가벼운 사람 두 명 무게합이 limit보다 작으면 필요 보트 수가 하나 줄어듬
        if people[start] + people[end] <= limit:
            end -= 1
            boat_cnt -= 1
        start += 1
    return boat_cnt


print(solution([70, 50, 80, 50], 100))