class Solution:
    def advantageCount(self, A, B):
        order = [i for i in range(len(B))]
        ans = [0 for _ in range(len(B))]
        order.sort(key=lambda x: -B[x])
        A.sort()
        for ord in order:
            ans[ord] = A.pop() if A[-1] > B[ord] else A.pop(0)

        return ans


s = Solution()
print(s.advantageCount([2,0,4,1,2], [1,3,0,0,2]))