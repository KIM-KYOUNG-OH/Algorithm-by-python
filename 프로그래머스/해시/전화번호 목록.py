# def solution(phone_book):
#     phone_book.sort()
#     for i in range((len(phone_book))):
#         key = phone_book[i] # key = phone_book의 요소
#         temp = list(phone_book)
#         temp.pop(i)
#         for j in range(len(temp)):
#             if key == temp[j][:len(key)]: # phone_book 요소중 key의 길이만큼 문자열을 slicing
#                 return False
#     return True

def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    for i in range(0, len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            for k in range(len(phone_book[i])):
                if phone_book[i][k] != phone_book[j][k]:
                    break
                
    return answer

print(solution(["119", "97674223", "1195524421"]))


