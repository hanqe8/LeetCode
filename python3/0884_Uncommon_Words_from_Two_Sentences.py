class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count1, count2 = set([i for i, j in sorted(Counter(s1.split()).items()) if j == 1]), set([i for i, j in sorted(Counter(s2.split()).items()) if j == 1])
        list1, list2, soln = list(count1), list(count2), []
        for i in list1:
            if i not in s2.split():
                soln.append(i)
        for j in list2:
            if j not in s1.split():
                soln.append(j)
        return list(set(soln))
