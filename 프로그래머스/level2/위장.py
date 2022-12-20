from collections import defaultdict


def solution(clothes):
    clothes_dic = defaultdict(int)
    for name, type in clothes:
        clothes_dic[type] += 1

    answer = 1
    for key in clothes_dic.keys():
        answer *= clothes_dic[key] + 1
    return answer - 1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])