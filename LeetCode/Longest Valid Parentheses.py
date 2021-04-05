class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        answer = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack[-1]!=-1 and s[stack[-1]] == '(':
                stack.pop()
                answer = max(answer, i-stack[-1])
            else:
                stack.append(i)

        return answer

sol = Solution()
print(sol.longestValidParentheses("(()"))