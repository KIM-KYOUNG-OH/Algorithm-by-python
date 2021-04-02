class Solution:
    def maxEnvelopes(self, envelopes: list) -> int:
        envelopes.sort(key = lambda x:(x[0],x[1]))
        w,h = -1,-1
        count = 0
        print(envelopes)
        for envelope in envelopes:
            temp_w, temp_h = envelope[0], envelope[1]
            if w < temp_w and h < temp_h:
                count += 1
                w, h = temp_w, temp_h
        return count


s = Solution()
print(s.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))