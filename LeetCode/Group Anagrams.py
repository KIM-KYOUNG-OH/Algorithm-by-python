class Solution:
    def groupAnagrams(self, strs):
        lst = []
        for s in strs:
            temp = sorted([s[i] for i in range(len(s))])
            temp = ''.join(temp)
            lst.append((temp, s))
        lst = sorted(lst)

        result = []
        temp = []
        cur = '0'
        for group, s in lst:
            if cur == '0':
                cur = group
                temp.append(s)
            elif cur == group:
                temp.append(s)
            else:
                cur = group
                result.append(temp)
                temp = [s]
        if temp:
            result.append(temp)
        return result
