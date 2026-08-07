class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = {}
        freq = [[] for i in range(len(nums)+1)] 
        for n in nums:
            c_map[n] = c_map.get(n,0) + 1
        for num, count in c_map.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)                
                if len(res) == k:
                    return res


