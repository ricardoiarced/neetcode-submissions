class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # input = ["apple", "app", "ap"] output = "ap"
        if not strs:
            return ""

        res = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(res)):
                if strs[i][j] == res[j]:
                    j += 1
                else:
                    break
            res = res[:j]
        return res
