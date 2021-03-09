import collections

def solution(numbers, target):
    answer = 0
    # [현재까지 합, 합한 성분 개수]
    q = collections.deque([(0, 0)])
    # 큐가 다 비워질때까지
    while q:
        current_sum, num_idx = q.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            # 하나 빼고 두개 생성
            number = numbers[num_idx]
            q.append((current_sum+number, num_idx + 1))
            q.append((current_sum-number, num_idx + 1))

    return answer