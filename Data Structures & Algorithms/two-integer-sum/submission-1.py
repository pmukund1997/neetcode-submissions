class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = dict()
        for i, num in enumerate(nums):
            nums_map[num] = i

        for index,val in enumerate(nums):
            second_num = target - val
            second_num_index = nums_map.get(second_num, False)
            if second_num_index and second_num_index != index:
                return [index, second_num_index]
            
        return []

        