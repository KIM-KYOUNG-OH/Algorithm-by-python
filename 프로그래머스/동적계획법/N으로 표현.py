# def solution(N, number):
#     s = [0,{N}]
#     if N == number:
#         return 1
#     for i in range(2,9):
#         case_set = {int(str(N)*i)}
#         for j in range(1,i//2+1):
#             for x in s[j]:
#                 for y in s[i-j]:
#                     case_set.add(x+y)
#                     case_set.add(x-y)
#                     case_set.add(y-x)
#                     case_set.add(x*y)
#                     if x!=0:
#                         case_set.add(y//x)
#                     if y!=0:
#                         case_set.add(x//y)
#         if number in case_set:
#             return i
#         s.append(case_set)
#     return -1

def solution(N, number):
    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):  # S[i_half] S[1]
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x) # y-x 케이스 추가
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
    return -1


print(solution(5,12))