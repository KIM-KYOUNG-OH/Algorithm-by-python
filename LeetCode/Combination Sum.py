class Solution:
    def combinationSum(self, candidates, target: int):
        dp = [[] for _ in range(target + 1)]
        for num in candidates:
            if num > target:
                continue
            dp[num].append(tuple([num]))

        for i in range(1, target + 1):
            print('i = ', i)
            for e in dp[i]:
                for num in candidates:
                    temp = list(e)
                    temp.append(num)
                    total = sum(temp)
                    if total > target:
                        continue
                    temp = tuple(sorted(temp))
                    if temp not in dp[total]:
                        dp[total].append(temp)
            print(dp)
        return list(map(list, sorted(dp[target])))


print(Solution.combinationSum('', [7,3,9,6], 6))