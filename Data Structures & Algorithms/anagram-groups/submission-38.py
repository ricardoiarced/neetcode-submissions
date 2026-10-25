class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #["ate", "eta", "pan", "nap"]

        res = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted not in res:
                res[word_sorted] = []
            res[word_sorted].append(word)
        return list(res.values())