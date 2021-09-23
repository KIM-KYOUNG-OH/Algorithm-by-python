from collections import deque


def solution(jobs):
    answer = []
    current_time = 0
    current_classification = -1
    waiting_queue = deque([])
    waiting_importance_dic = dict()
    working = []
    while jobs:
        if current_time >= jobs[0][0]:
            request_time, elapsed_time, classification, importance = jobs.pop(0)
            waiting_queue.append((request_time, elapsed_time, classification, importance))
            if classification not in waiting_importance_dic:
                waiting_importance_dic[classification] = importance
            else:
                waiting_importance_dic[classification] += importance
            if jobs:
                continue
        if not working:
            if current_classification == -1:
                request_time, elapsed_time, classification, importance = waiting_queue.popleft()
                current_classification = classification
                waiting_importance_dic[classification] -= importance
                answer.append(classification)
            else:
                for job in waiting_queue:
                    if job[2] == current_classification:

    return answer