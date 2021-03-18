def solution(s):
    lst = list(map(int, s.split(" ")))
    min_num = str(min(lst))
    max_num = str(max(lst))

    return min_num +" "+ max_num

print(solution("1 2 3 4"))