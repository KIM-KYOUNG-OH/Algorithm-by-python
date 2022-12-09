from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    q = deque()
    answer = 0
    for city in cities:
        city = city.lower()
        if city not in q:
            if len(q) < cacheSize:
                q.append(city)
            else:
                q.popleft()
                q.append(city)
            answer += 5
        else:
            q.remove(city)
            q.append(city)
            answer += 1
    print(answer)
    return answer


solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	)
