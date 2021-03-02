def solution(answers):
    answer = []
    correct_one = 0
    correct_two = 0
    correct_three = 0

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            correct_one += 1
        if answers[i] == two[i%len(two)]:
            correct_two += 1
        if answers[i] == three[i%len(three)]:
            correct_three += 1
    temp = [correct_one, correct_two, correct_three]

    for key, value in enumerate(temp):
        if max(temp) == value:
            answer.append(key+1)
    return answer

print(solution([1,3,2,4,2]))