def solution(clothes):
    data = dict()
    count = 1
    for i in clothes:
        if i[1] in data:
            data[i[1]] += 1
        else:
            data[i[1]] = 1
    # {'headgear': 2, 'eyewear': 1}
    for i in data.values():
        count *= (i+1)
    count -= 1 # count = (모자+1)*(안경+1) - 1 : 아무것도 안입은 경우의 수 1을 빼준다

    return count


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))