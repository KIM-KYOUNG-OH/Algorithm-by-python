def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]: # 순서가 다른 순간 i번째가 답
            return participant[i]
    return participant[-1] # 전부 일치하면 마지막에 남은애가 답

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
