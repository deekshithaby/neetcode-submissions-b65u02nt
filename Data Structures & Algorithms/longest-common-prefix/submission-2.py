class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i, s in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return ans
                if s != strs[j][i]:
                    return ans
            ans += s

        return ans