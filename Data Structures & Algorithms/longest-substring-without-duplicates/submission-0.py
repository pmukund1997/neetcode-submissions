class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r  = 0 , 0
        max_length = 0
        c = set()

        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l += 1
            w = (r-l) + 1
            max_length = max(max_length, w)
            c.add(s[r])

        return max_length


         