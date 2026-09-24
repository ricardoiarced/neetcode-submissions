class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in res.keys():
                return [res[complement], i]
            res[val] = i