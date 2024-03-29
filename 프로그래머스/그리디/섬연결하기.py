# def solution(n, costs):
#     # kruskal algorithm
#     ans = 0
#     costs_sort = sorted(costs,key=lambda x: x[2]) # cost 기준으로 오름차순 정렬
#     routes = set([costs_sort[0][0]]) # 집합
#     while len(routes)!=n:
#         for i, cost in enumerate(costs_sort):
#             if cost[0] in routes and cost[1] in routes:
#                 continue
#             if cost[0] in routes or cost[1] in routes:
#                 routes.update([cost[0], cost[1]])
#                 ans += cost[2]
#                 break
#     return ans

def solution(n, costs):
    # answer = 0  # 최소 비용
    # costs_sorted = sorted(costs, key=lambda x: x[2])  # 비용순 오름차순 정렬
    # paths = {costs_sorted[0][0]}
    # for cost in costs_sorted:
    #     if len(paths) == n:
    #         break
    #     if cost[0] in paths and cost[1] in paths:  # 이미 두 섬을 잇는 path가 저장됨
    #         continue
    #     if cost[0] in paths or cost[1] in paths:  # 두 섬을 잇는 path 저장
    #         paths.add(cost[0])
    #         paths.add(cost[1])
    #         answer += cost[2]  # 비용 더하기

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    answer = 0  # 최소 비용

    parent = [i for i in range(n)]

    costs_sorted = sorted(costs, key=lambda x: x[2])  # 비용순 오름차순 정렬

    for edge in costs_sorted:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 아닐 경우에만 추가
            union_parent(parent, a, b)
            answer += cost
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))