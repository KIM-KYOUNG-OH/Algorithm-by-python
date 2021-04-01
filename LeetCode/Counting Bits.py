class Solution:
    def countBits(self, num):
        answer = []
        for i in range(num + 1):
            answer.append(format(i, 'b').count('1'))
        return answer
