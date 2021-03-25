from itertools import permutations

def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    elif priority[n] == "*":
        return str(eval('*'.join([calc(priority, n+1, e) for e in expression.split("*")])))
    elif priority[n] == "+":
        return str(eval('+'.join([calc(priority, n + 1, e) for e in expression.split("+")])))
    elif priority[n] == "-":
        return str(eval('-'.join([calc(priority, n+1, e) for e in expression.split("-")])))

def solution(expression):
    answer = 0
    priority = list(permutations(['+','-','*'],3))
    for p in priority:
        answer = max(answer, abs(int(calc(p, 0, expression))))

    return answer

print(solution("100-200*300-500+20"))