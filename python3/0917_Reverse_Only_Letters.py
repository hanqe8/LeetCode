class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # using two pointer method:
        anchor, pointer = 0, len(s)-1
        sList = list(s)
        while anchor < pointer:
            if sList[anchor].isalpha():
                if sList[pointer].isalpha():
                    sList[anchor], sList[pointer] = sList[pointer], sList[anchor]
                    anchor += 1
                    pointer -= 1
                else:
                    pointer -= 1
            else:
                anchor += 1
        return ''.join(sList)
      
        # by iterating through the string:
        alphaList, soln, count = [], [], 0
        for letter in s:
            if letter.isalpha():
                alphaList.append(letter)
        reversedAlphaList = alphaList[::-1]
        for i in range(len(s)):
            if s[i].isalpha():
                soln.append(reversedAlphaList[count])
                count += 1
            else:
                soln.append(s[i])
        return ''.join(soln)
