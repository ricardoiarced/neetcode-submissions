class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freq.append([cnt, num])
        
        freq.sort()

        res = []
        for i in range(len(freq)):
            res.append(freq.pop()[1])
            if len(res) == k:
                return res