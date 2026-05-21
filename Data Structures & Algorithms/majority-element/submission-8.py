class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            count = sum(1 for i in nums if i == num)
            if count > len(nums) // 2:
                return num