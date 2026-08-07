class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for i in nums:
            if seen.get(i):
                return True
            else:
                seen[i] = 1
        
        return False

