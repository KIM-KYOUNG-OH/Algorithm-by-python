def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(w,h):
    if w > h:
        w, h = h, w
    g = gcd(h, w)
    return h * w - (h // g + w // g - 1) * g