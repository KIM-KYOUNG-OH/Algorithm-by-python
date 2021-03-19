def solution(dirs):
    command = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    path_set = set()
    current_posx, current_posy = 0,0
    for alp in dirs:
        after_posx, after_posy = current_posx+command[alp][0], current_posy+command[alp][1]
        if -5 <= after_posx <= 5 and -5 <= after_posy <= 5:
            # 방향이 다른 두개의 경로를 set에 add하는 것이 핵심
            path_set.add((current_posx, current_posy, after_posx, after_posy))
            path_set.add((after_posx, after_posy, current_posx, current_posy))
            current_posx, current_posy = after_posx, after_posy

    return len(path_set) // 2

print(solution("ULURRDLLU"))