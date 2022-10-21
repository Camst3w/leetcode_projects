# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slow = head
        stack = []

        while slow != None:
            stack.append(slow.val)
            slow = slow.next

        for i in range(len(stack)//2):
            head = head.next
        return head


