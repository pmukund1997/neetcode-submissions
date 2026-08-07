class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,num in enumerate(nums):
            e = target - num
            for j, f in enumerate(nums):
                if index != j:
                    if f == e:
                        return [index, j]
        return []

        