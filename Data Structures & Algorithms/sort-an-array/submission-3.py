class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2

            divide(arr, l, m)
            divide(arr, m+1, r)
            mergeSort(arr, l, m, r)
        
        def mergeSort(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = 0, 0, l

            while i < len(left) and j < len(right):
                if right[j] < left[i]:
                    arr[k] = right[j]
                    j += 1
                else:
                    arr[k] = left[i]
                    i += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
        divide(nums, 0, len(nums) - 1)
        return nums