# from itertools import combinations
#
# while True:
#     request = list(map(int, input().split()))
#     if len(request) == 1 and request[0] == 0:
#         break
#     k = request[0]
#     numbers = request[1:]
#     comb_numbers = combinations(numbers, 6)
#     for data in comb_numbers:
#         print(' '.join(map(str, data)))
#     print()

def lotto(start, depth):
    if depth == 6:
        for num in combination:
            print(num, end=' ')
        print()
        return
    for i in range(start, len(numbers)):
        combination[depth] = numbers[i]
        lotto(i+1, depth+1)


while True:
    numbers = list(map(int, input().split()))
    k = numbers.pop(0)
    if k == 0:
        break
    combination = [0] * 6
    lotto(0, 0)
    print()