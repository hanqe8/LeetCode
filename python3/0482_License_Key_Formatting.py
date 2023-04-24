class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s, newString = s.replace("-","")[::-1], ''
        if len(s)%k == 0: # settle cases where exact multiple
            endRange = len(s)
        else:
            endRange = len(s)//k + 1
        j = 0
        for i in range(0, endRange): # instead of using j, can use range(0, endRange, k) and modify endRange
            newString += (s[j:k+j] + "-") 
            j += k # increment slice index by step k
        return newString[::-1].strip("-").upper() # return and strip leading hyphens and capitalise lowercase
