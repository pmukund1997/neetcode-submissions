from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequncy_map = Counter(nums)
        n_len = len(nums)
        buckets = [0] * (n_len + 1)

        for num, freq in frequncy_map.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
            
        result = [] 
        for i in range(n_len, -1, -1):
            if buckets[i] != 0:
                result.extend(buckets[i])
            if len(result) == k:
                break

        return result

        
        