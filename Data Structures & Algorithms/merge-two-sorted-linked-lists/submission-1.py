class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2

        dummy = ListNode(0)
        currentRes = dummy
        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val <= current2.val:
                currentRes.next = current1
                current1 = current1.next
            else:
                currentRes.next = current2
                current2 = current2.next
            currentRes = currentRes.next

        if current1:
            currentRes.next = current1
        if current2:
            currentRes.next = current2

        return dummy.next