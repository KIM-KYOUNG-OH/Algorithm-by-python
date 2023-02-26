def getMid(bin_num):
    if len(bin_num) == 1:
        return bin_num
    mid_idx = len(bin_num) // 2
    mid = bin_num[mid_idx]
    left = bin_num[:mid_idx]
    if not getMid(left) or (getMid(left) == '1' and mid == '0'):
        return False
    right = bin_num[mid_idx + 1:]
    if not getMid(right) or (getMid(right) == '1' and mid == '0'):
        return False
    return mid


def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = bin(number)[2:]
        binary_tree_size = 1
        while binary_tree_size < len(bin_num):
            binary_tree_size = (binary_tree_size + 1) * 2 - 1
        bin_num = '0' * (binary_tree_size - len(bin_num)) + bin_num

        if getMid(bin_num):
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution([7, 42, 5]))