class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # iterate through each list method
        word, idx, soln = [], [], []
        for i in list1:
            if i in list2:
                idx.append(list1.index(i)+list2.index(i))
                word.append(i)
        for k in [j for j, x in enumerate(idx) if x == min(idx)]:
            soln.append(word[k])
        return soln
      
        # alternative method: enumerate dict, set
        common, index_dict = set(list1).intersection(set(list2)), {} # define common as intersection between both lists
        for idx, i in enumerate(list1): # enumerate through each list and if word exists in intersection, create entry in dictionary where key = word, value = index
            if i in common:
                index_dict[i] = idx
        for idx1, j in enumerate(list2):
            if j in common:
                index_dict[j] += idx1 # if word from list2 in intersection, add list2 index value to existing value for key
        return [word for word, k in index_dict.items() if k == min(index_dict.values())] # for each item value in dict, if equals to min, return key (key, value)

        
