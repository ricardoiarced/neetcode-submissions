class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in res and res[diff] != i:
                return [res[diff], i]
            
            res[num] = i