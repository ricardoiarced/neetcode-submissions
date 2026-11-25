class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_counts = {0:1}
        total = 0
        matches = 0

        for num in nums:
            total += num
            matches += prefix_counts.get(total - k, 0)
            prefix_counts[total] = prefix_counts.get(total, 0) + 1

        return matches