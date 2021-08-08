# def solution(routes):
#     routes.sort(key=lambda x:x[1])
#     camera = -30001
#     answer = 0
#     for i in routes:
#         if i[0] > camera:
#             answer += 1
#             camera = i[1]
#     return answer

def solution(routes):
    routes.sort(key=lambda x: x[1])
    prev_camera_pos = -30001
    camera_cnt = 0
    for route in routes:
        if prev_camera_pos < route[0]:
            prev_camera_pos = route[1]
            camera_cnt += 1
    return camera_cnt


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))