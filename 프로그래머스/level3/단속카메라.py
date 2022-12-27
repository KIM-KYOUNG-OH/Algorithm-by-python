def solution(routes):
    routes.sort(key=lambda x: -x[0])
    camera = 30001
    answer = 0
    for s, e in routes:
        if camera > e:
            camera = s
            answer += 1
    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))