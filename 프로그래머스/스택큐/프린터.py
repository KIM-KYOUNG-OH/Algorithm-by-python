from collections import deque


def solution(priorities, location):
    answer = 0  # 프린터 대기수
    priorities_stack = sorted(priorities)  # 스택(우선순위 오름차순 정렬)
    priorities_queue = deque()  # 큐
    for i in range(len(priorities)):
        priorities_queue.append((i, priorities[i]))
    while True:
        head = priorities_queue.popleft()  # queue의 맨앞 노드
        if priorities_stack[-1] != head[1]:  # stack의 peek가 head와 다를 때
            priorities_queue.append(head)  # head를 queue의 맨뒤로 옮기기
            continue
        if priorities_stack[-1] == head[1]:  # stack의 peek가 head와 같을 때
            answer += 1
            priorities_stack.pop()  # stack의 peek값 pop하기
        if head[0] == location:  # popleft한 head의 index가 문제에서 요구한 location일 때
            break

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))