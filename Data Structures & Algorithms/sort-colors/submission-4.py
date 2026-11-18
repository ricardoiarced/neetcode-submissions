class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, scan, high = 0, 0, len(nums) - 1
        while scan <= high:
            if nums[scan] == 0:
                nums[low], nums[scan] = nums[scan], nums[low]
                low += 1
                scan += 1
            elif nums[scan] == 1:
                scan += 1
            else:
                nums[high], nums[scan] = nums[scan], nums[high]
                high -= 1