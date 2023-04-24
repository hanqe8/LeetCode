class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        soln, newWords = [], [word.lower() for word in words]
        keyDict = {1: set("qwertyuiop"), 2: set("asdfghjkl"), 3: set("zxcvbnm")}
        for i in range(len(newWords)):
            if len(set(newWords[i])-keyDict[1]) == 0 or len(set(newWords[i])-keyDict[2]) == 0 or len(set(newWords[i])-keyDict[3]) == 0:
                soln.append(words[i])
        return soln
