class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        i, m, M = 0, min(strs), max(strs)
        for j in range(min(len(m), len(M))):
            if m[j] == M[j]:
                i += 1
            else:
                break
        return m[:i]
