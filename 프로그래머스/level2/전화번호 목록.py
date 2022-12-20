def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        a = phone_book[i]
        b = phone_book[i + 1]
        if b[:len(a)] == a:
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))