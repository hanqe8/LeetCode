class Solution:
    def firstUniqChar(self, s: str) -> int:

        # iterative loop causes timeout for longer string
        seen, slist, count = [], list(s), 0
        while count < len(s):
            for index, i in enumerate(slist):
                if i in list(s)[index+1::] or i in seen:
                    seen.append(slist[index])
                    count += 1
                else:
                    return index
        return -1
      
        # use collection to obtain unique characters in string + count
        countdict = collections.Counter(s)
        for i in range(len(s)):
            if countdict[s[i]] == 1:
                return i
        return -1
