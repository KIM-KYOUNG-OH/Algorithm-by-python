import sys


def is_palindrome(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def check(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            check1 = is_palindrome(word, left + 1, right)
            check2 = is_palindrome(word, left, right - 1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0


n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    left = 0
    right = len(word) - 1
    ans = check(word, left, right)
    print(ans)