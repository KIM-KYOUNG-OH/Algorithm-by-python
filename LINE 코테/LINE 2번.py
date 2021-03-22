def check1(s,answer):
    if 8 >= len(s) or len(s) >= 15:
        answer.append(1)

def check23(s,answer):
    cnt_lst=[0,0,0,0]
    specials="~!@#$%^&*"
    for ch in list(s):
        if 65 <= ord(ch) <= 90:
            cnt_lst[0]+=1
        elif 97 <= ord(ch) <= 122:
            cnt_lst[1]+=1
        elif 48 <= ord(ch) <= 57:
            cnt_lst[2]+=1
        elif ch in list(specials):
            cnt_lst[3]+=1
        else:
            if 2 not in answer:
                answer.append(2)
    if cnt_lst.count(0)>1:
        answer.append(3)

def check4(s,answer):
    before = " "
    repeat_cnt = 1
    for ch in list(s):
        if before == ch:
            repeat_cnt+=1
        else:
            repeat_cnt = 1
        if repeat_cnt >= 4:
            answer.append(4)
            break
        before = ch

def check5(s,answer):
    m = list(s)
    m.sort()
    before = " "
    repeat_cnt = 1
    for ch in list(m):
        if before == ch:
            repeat_cnt+=1
        else:
            repeat_cnt = 1
        if repeat_cnt >= 5:
            answer.append(5)
            break
        before = ch

def solution(inp_str):
    answer = []
    check1(inp_str,answer)
    check23(inp_str, answer)
    check4(inp_str, answer)
    check5(inp_str, answer)

    if len(answer) == 0:
        answer.append(0)
    return answer

print(solution("UUUUU"))