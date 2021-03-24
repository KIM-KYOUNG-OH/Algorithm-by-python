from itertools import combinations_with_replacement
from collections import Counter

class Solution:
    def threeSumMulti(self, arr, target):
        dic = Counter(arr)
        res = 0
        print(dict(dic))
        print(list(combinations_with_replacement(dic.keys(), 2)))
        for i, j in combinations_with_replacement(dic.keys(), 2):
            k = target-i-j
            if i==j==k:
                res += dic[i]*(dic[i]-1)*(dic[i]-2)/6
            elif i==j!=k:
                res += dic[i]*(dic[i]-1)/2*dic[k]
            elif k>i and k>j:
                res += dic[i]*dic[j]*dic[k]

        return int(res%(10**9+7))


s = Solution()
print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))