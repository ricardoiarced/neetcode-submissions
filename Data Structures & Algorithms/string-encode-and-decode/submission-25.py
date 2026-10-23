class Solution:

    def encode(self, strs: List[str]) -> str:
        # decode(encode(strs)) = strs
        result = []
        for word in strs:
            result.append(str(len(word)) + "#" + word)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
        
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            result.append(s[i:i + length])

            i += length
        return result
