class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'(' : ')', '[' : ']', '{' : '}'}
        list1 = []
        for i in s:
            if i in bracket_dict:
                list1.append(i)
            elif len(list1) == 0 or bracket_dict[list1.pop()] != i:
                return False
        return len(list1) == 0
