class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        n = len(nums)
        i = 0
        while i < n:
            ans[i] = nums[i]
            ans[i + n] = nums[i]
            i += 1
        return ans