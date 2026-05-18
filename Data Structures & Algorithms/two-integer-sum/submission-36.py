class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in res and res[complement] != i:
                return sorted([i, res[complement]])