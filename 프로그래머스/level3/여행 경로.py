def solution(tickets):
    def dfs(n, visited, path, depth):
        if depth == n:
            candidates.append(path)
            return
        next = path[-3:]
        for i in range(n):
            ticket = tickets[i]
            if not visited[i] and ticket[0] == next:
                visited[i] = True
                dfs(n, visited, path + ',' + ticket[1], depth + 1)
                visited[i] = False


    candidates = []
    n = len(tickets)
    visited = [False] * n
    for i in range(n):
        ticket = tickets[i]
        if ticket[0] == 'ICN':
            visited[i] = True
            dfs(n, visited, 'ICN,' + ticket[1], 1)
            visited[i] = False
    candidates.sort()
    return candidates[0].split(',')


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
