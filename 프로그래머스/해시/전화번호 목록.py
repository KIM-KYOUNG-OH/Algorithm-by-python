# # def solution(phone_book):
# #     phone_book.sort()
# #     for i in range((len(phone_book))):
# #         key = phone_book[i] # key = phone_book의 요소
# #         temp = list(phone_book)
# #         temp.pop(i)
# #         for j in range(len(temp)):
# #             if key == temp[j][:len(key)]: # phone_book 요소중 key의 길이만큼 문자열을 slicing
# #                 return False
# #     return True
#
# def solution(phone_book):
#     phone_book.sort()  # 문자열 배열의 sort()는 아스키 코드표순 정렬
#     for i in range(len(phone_book) - 1):  # sort()했기 때문에 접두어 관계끼리는 붙어있다.
#         if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
#             return False
#     return True
#
# print(solution(["119", "97674223", "1195524421"]))
#
#

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        cur = phone_book[i]
        next = phone_book[i + 1]
        if cur == next[:len(cur)]:
            return False
    return True
