class Solution:
    def check_and_add(self, map,val):
        if map.get(val):
            map[val] += 1
        else:
            map[val] = 1
    def isAnagram(self, s: str, t: str) -> bool:
        flen = len(s)
        if flen != len(t):
            return False
        f_hash = dict()
        s_hash = dict()
        for i in range(flen):
            self.check_and_add(f_hash, s[i])
            self.check_and_add(s_hash, t[i])
        if f_hash == s_hash:
            return True
        return False





        