class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(arr, l, r):
            if l == r:
                return
            m = (l + r) // 2
            divide(arr, l, m)
            divide(arr, m + 1, r)
            merge(arr, l, m, r)
        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = 0, 0, l

            while j < len(left) and i < len(right):
                if left[j] < right[i]:
                    arr[k] = left[j]
                    j += 1
                else:
                    arr[k] = right[i]
                    i += 1
                k += 1
            
            while j < len(left):
                arr[k] = left[j]
                j += 1
                k += 1
            
            while i < len(right):
                arr[k] = right[i]
                i += 1
                k += 1
        divide(nums, 0, len(nums) - 1)

        return nums