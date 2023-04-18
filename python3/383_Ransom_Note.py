class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # use iteration through ransomNote and remove from list of magazine elements
        rnList, magList = [], list(magazine)
        if len(ransomNote) > len(magazine):
            return False
        for i in ransomNote:
            try:
                magList.remove(i)
            except ValueError:
                return False
        return True
      
      # alternatively, count no. of elements per str and compare elements and count
      rnCount, magCount = Counter(ransomNote), Counter(magazine)
      return rnCount & magCount == rnCount
