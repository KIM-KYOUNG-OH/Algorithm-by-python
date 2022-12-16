def solution(info, edges):
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, cur in edges:
            isWolf = info[cur]
            if visited[parent] and not visited[cur]:
                visited[cur] = True
                if isWolf == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[cur] = False

    visited = [False] * len(info)
    visited[0] = True
    answer = []
    dfs(1, 0)
    return max(answer)


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))