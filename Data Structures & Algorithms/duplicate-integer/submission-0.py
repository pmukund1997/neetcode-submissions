class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            count = 0 
            for fnum in nums:
                if num == fnum:
                    count += 1
            if count > 1:
                return True
        return False