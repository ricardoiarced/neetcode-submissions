class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        unique = list(res.keys())
        unique.sort(key=lambda x: res[x], reverse=True)
        return unique[:k]