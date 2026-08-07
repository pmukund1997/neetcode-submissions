class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for ch in s:
            if s_map.get(ch):
                s_map[ch] += 1
            else:
                s_map[ch] = 1
        for c in t:
            if t_map.get(c):
                t_map[c] +=1
            else:
                t_map[c] = 1
        for char in s_map:
            if s_map[char] != t_map.get(char,0):
                return False
        return True