# from itertools import permutations
#
# def count_prime(num_case):
#     prime_count = 0
#     for n in num_case:
#         count = 0
#         for i in range(2, n): # 2부터 n-1까지 나누었을때 나머지가 전부 0이 아니면 소수
#             if n%i == 0:
#                 count+=1
#                 break
#         if n>1 and count==0:
#             prime_count += 1
#     return prime_count
#
# def solution(numbers):
#     num_case = []
#     for i in range(1,len(numbers)+1):
#         tmp = permutations(numbers, i)
#
#         for n in tmp:
#             tmp_str = "".join(n)
#             num_case.append(int(tmp_str))
#     num_case = list(set(num_case)) # 중복 없앰
#     return count_prime(num_case)
import itertools


def solution(numbers):
    is_prime = [True] * int(1e7)  # 1 ~ 9999999 까지 소수판별 리스트 선언
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(len(is_prime) ** 0.5) + 1):  # 에라토스테네스의 체
        if not is_prime[i]:
            continue
        for j in range(i + i, len(is_prime), i):
            if is_prime[j]:
                is_prime[j] = False

    numbers = list(numbers)
    candidates = set()  # 모든 경우의 수
    for i in range(1, len(numbers) + 1):
        cases = list(itertools.permutations(numbers, i))  # 순열로 i만큼의 길이를 가진 모든 경우의 수 정의
        for case in cases:
            candidates.add(int(''.join(case)))  # 문자 리스트에서 int로 변환하여 저장

    answer = 0  # 소수의 개수
    for candidate in list(candidates):
        if is_prime[candidate]:  # 미리 찾아놓은 소수 판별 리스트에 대조
            answer += 1

    return answer


print(solution("17"))