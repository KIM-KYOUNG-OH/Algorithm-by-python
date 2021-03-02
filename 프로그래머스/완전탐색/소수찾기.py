from itertools import permutations

def count_prime(num_case):
    prime_count = 0
    for n in num_case:
        count = 0
        for i in range(2, n): # 2부터 n-1까지 나누었을때 나머지가 전부 0이 아니면 소수
            if n%i == 0:
                count+=1
                break
        if n>1 and count==0:
            prime_count += 1
    return prime_count

def solution(numbers):
    num_case = []
    for i in range(1,len(numbers)+1):
        tmp = permutations(numbers, i)

        for n in tmp:
            tmp_str = "".join(n)
            num_case.append(int(tmp_str))
    num_case = list(set(num_case)) # 중복 없앰
    return count_prime(num_case)

print(solution("17"))