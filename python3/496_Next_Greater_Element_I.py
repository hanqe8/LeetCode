class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # due to poorly defined question in Leetcode, this solution resovles if checking if element nums2[j+1] is greater than nums1[i]
        # nums1[i] == nums2[j] and nums2[j+1] > nums1[i]
        soln = []
        for i in range(len(nums1)):
            if nums2.index(nums1[i]) + 2 > len(nums2) or nums2[nums2.index(nums1[i])+1] < nums1[i]:
                soln.append(-1)
            else:
                soln.append(nums2[nums2.index(nums1[i])+1])
        return soln
      
        # testcases in question ask to resolve and check if any 1 element in nums2[j:] is greater than nums1[i]
        soln = []
        for i in range(len(nums1)):
            if nums2.index(nums1[i]) + 2 > len(nums2) or max(nums2[nums2.index(nums1[i])+1:]) < nums1[i]: 
                soln.append(-1)
            else:
                soln.append(max(nums2[nums2.index(nums1[i])+1:]))
        return soln
