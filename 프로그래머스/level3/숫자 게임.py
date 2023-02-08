def upper_bound(B, target):
    left = 0
    right = len(B) - 1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        # print('left = ', left, ', right = ', right, ', mid = ', mid)
        if B[mid] > target:
            right = mid - 1
            answer = mid
        elif B[mid] < target:
            left = mid + 1
        else:
            left = mid + 1
    if answer >= len(B):
        answer -= 1
    return answer


def canWin(B, target):
    # print(B)
    delIdx = upper_bound(B, target)
    # print('target = ', target, ', delIdx = ', delIdx)
    if B[delIdx] - target > 0:
        del B[delIdx]
        return True
    else:
        del B[0]
        return False


def solution(A, B):
    B.sort()
    score = 0
    for a in A:
        if canWin(B, a):
            score += 1
    return score


print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))
