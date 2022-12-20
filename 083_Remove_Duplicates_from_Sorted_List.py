class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # since linked list is sorted, iterate through to find duplicates and add non-duplicates to new list
        new_list = head
        while head and new_list.next:
            if new_list.val == new_list.next.val:
                new_list.next = new_list.next.next
            else:
                new_list = new_list.next
        return head
