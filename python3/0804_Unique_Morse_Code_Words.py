class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-", "-.--","--.."]
        soln = []
        if len(words) == 1: return 1 # not necessary since below will take care of case
        for word in words:
            j = [morseList[ord(i)-97] for i in word] # ord() - 97 to return ASCII mapping for lowercase alphabets and index to 0
            if ''.join(j) not in soln: # if morse code not present in soln, append to list
                soln.append(''.join(j))
        return len(soln) # return total variations
