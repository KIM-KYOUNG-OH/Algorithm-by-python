# def solution(people, limit):
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b:
#         if people[b] + people[a] <= limit:
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer

def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    j = len(people) - 1
    for i in range(len(people)):
        if i > j:
            break
        elif i == j:
            answer += 1
            break
        tmp = people[i]
        while tmp + people[j] <= limit:
            tmp += people[j]
            j -= 1
        answer += 1
    return answer


# print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
