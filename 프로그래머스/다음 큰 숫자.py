def binary_scale(x):
    result = ""
    while True:
        result += str(x%2)
        x //= 2
        if x == 0:
            break
    return result[::-1]

def solution(n):
    cnt_n = binary_scale(n).count("1")
    num = n
    while True:
        num += 1
        if cnt_n == binary_scale(num).count("1"):
            return num