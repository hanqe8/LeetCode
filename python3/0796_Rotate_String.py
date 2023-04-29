class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # iterate through list
        if len(s) == len(goal): # if unequal length = False
            for i in range(len(s)):
                s = s[1:len(s)] + s[0]
                if s == goal:
                    return True
        return False
      
        # alternative method: check if s exists in goal+goal (since rotation basis, joining 2 goal presents all rotations possible)
        return len(s) == len(goal) and s in goal+goal
        # checks both conditions of length and if s is possible by shifting position of element by 1 each time
