def solution(people, limit):
    people_sorted = sorted(people, reverse=True)
    count = len(people_sorted)
    start, end = 0, len(people_sorted)-1
    sum = 0
    while start < end:
        sum += start+end
        if sum <= limit:
            end -= 1
            count -= 1
        else:
            sum = 0
        start += 1

    return count

print(solution([70, 50, 80, 50], 100))