# def solution(clothes):
#     data = dict()
#     count = 1
#     for i in clothes:
#         if i[1] in data:
#             data[i[1]] += 1
#         else:
#             data[i[1]] = 1
#     # {'headgear': 2, 'eyewear': 1}
#     for i in data.values():
#         count *= (i+1)
#     count -= 1 # count = (모자+1)*(안경+1) - 1 : 아무것도 안입은 경우의 수 1을 빼준다
#     return count

def solution(clothes):
    answer = 1
    clothes_dic = dict()
    for cloth in clothes:
        cloth_name, cloth_kind = cloth
        if cloth_kind not in clothes_dic:  # 처음 나온 옷 종류일 때
            clothes_dic[cloth_kind] = 1
        else:  # 이미 나온적 있는 옷 종류일 때
            clothes_dic[cloth_kind] += 1
    clothes_cnt = list(clothes_dic.values())  # 종류별 옷 개수, 리스트로 변환
    for cnt in clothes_cnt:
        answer *= (cnt + 1)  # 옷 안입는 경우부터 종류별 옷 개수 곱해주기
    answer -= 1  # 아무 옷도 안 입는 경우의 수 빼기
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))