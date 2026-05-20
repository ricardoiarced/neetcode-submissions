class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, val in count.items():
            if val > (len(nums)/2):
                return key