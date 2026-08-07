class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_map = defaultdict(int)

        for n in nums:
            c_map[n] += 1

        sd = dict(sorted(c_map.items(), key= lambda item:item[1]))
        return list(sd)[-k:]
