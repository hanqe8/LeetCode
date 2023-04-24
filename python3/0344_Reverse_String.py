class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1] # use s[:] to edit in place byte-wise
        
        # alternative:
        s.reverse()
