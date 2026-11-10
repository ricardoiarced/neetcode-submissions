class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
            if res[nums[i]] > len(nums) // 2:
                return nums[i]
