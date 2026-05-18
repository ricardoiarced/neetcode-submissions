class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(prefix)):
                if prefix[j] == strs[i][j]:
                    j += 1
                else:
                    break
            prefix = prefix[:j]
        return prefix