class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node
        dummy = ListNode()
        current = dummy

        # Traverse both linked lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        # Attach the remaining nodes
        current.next = list1 if list1 else list2

        # Return the merged list
        return dummy.next