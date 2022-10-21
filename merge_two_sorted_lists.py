class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        merge_list = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                merge_list.next = list1.val
                list1, merge_list = list1.next, list1
            else:
                merge_list.next = list2
                list2, merge_list = list2.next, list2

        if list1 or list2:
            merge_list = list1 if list1 else list2

            return dummy.next
